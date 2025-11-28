import psycopg2


class DBFacade:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname='payment',
                user='postgres',
                password='postgres',
                host='localhost',
                port=5432
            )
            self.conn.autocommit = False
            self.cur = self.conn.cursor()
        except Exception as e:
            print("Ошибка подключения к БД:", e)
            raise

    def add_client(self):
        iban = input("Введите IBAN клиента: ")
        if iban == "":
            print("IBAN не может быть пустым.")
            return

        try:
            query = "INSERT INTO customer (iban) VALUES (%s) RETURNING customer_id;"
            self.cur.execute(query, (iban,))
            new_id = self.cur.fetchone()[0]
            self.conn.commit()
            print(f"Клиент создан: customer_id={new_id}, iban={iban}")
        except Exception as e:
            self.conn.rollback()
            print("Ошибка при добавлении клиента:", e)

    def add_unpaid_invoice(self):
        invoice_no = input("Введите номер фактуры (целое число): ")
        customer_id = input("Введите customer_id (id клиента): ")
        amount = input("Введите сумму (например 100.50): ")

        try:
            invoice_no_int = int(invoice_no)
            customer_id_int = int(customer_id)
            amount_val = float(amount)
        except ValueError:
            print("Ошибка: invoice_number и customer_id должны быть целыми числами, amount — число.")
            return

        try:
            self.cur.execute("SELECT customer_id FROM customer WHERE customer_id = %s;", (customer_id_int,))
            if self.cur.fetchone() is None:
                print("Клиент с таким customer_id не найден.")
                return

            self.cur.execute("SELECT 1 FROM unpaid_invoice WHERE invoice_number = %s;", (invoice_no_int,))
            if self.cur.fetchone():
                print("Ошибка: invoice_number уже существует в unpaid_invoice.")
                return

            self.cur.execute("SELECT 1 FROM paid_invoice WHERE invoice_number = %s;", (invoice_no_int,))
            if self.cur.fetchone():
                print("Ошибка: invoice_number уже существует в paid_invoice.")
                return

            self.cur.execute(
                "INSERT INTO unpaid_invoice (invoice_number, customer_id, amount) VALUES (%s, %s, %s);",
                (invoice_no_int, customer_id_int, amount_val)
            )
            self.conn.commit()
            print(f"Неоплаченная фактура {invoice_no_int} создана.")
        except Exception as e:
            self.conn.rollback()
            print("Ошибка при создании неоплаченной фактуры:", e)

    def list_unpaid_invoices(self):
        try:
            self.cur.execute("""
                SELECT u.invoice_number, u.customer_id, c.iban, u.amount
                FROM unpaid_invoice u
                LEFT JOIN customer c ON c.customer_id = u.customer_id
                ORDER BY u.invoice_number;
            """)
            rows = self.cur.fetchall()
            if not rows:
                print("Нет неоплаченных фактур.")
                return []
            print("invoice_number | customer_id | iban | amount")
            for r in rows:
                iban_display = r[2] if r[2] is not None else "NULL"
                print(f"{r[0]:14} | {r[1]:11} | {iban_display:16} | {r[3]:.2f}")
            return rows
        except Exception as e:
            print("Ошибка при получении неоплаченных фактур:", e)
            return []

    def pay_invoice(self):
        rows = self.list_unpaid_invoices()
        if not rows:
            return

        invoice_no = input("Введите invoice_number для оплаты (из списка выше): ")
        try:
            invoice_no_int = int(invoice_no)
        except ValueError:
            print("invoice_number должен быть целым числом.")
            return

        try:
            self.cur.execute(
                "SELECT invoice_number, customer_id, amount FROM unpaid_invoice WHERE invoice_number = %s FOR UPDATE;",
                (invoice_no_int,)
            )
            inv = self.cur.fetchone()
            if not inv:
                print("Не найдена неоплаченная фактура с таким invoice_number.")
                self.conn.rollback()
                return

            inv_number, customer_id, amount = inv

            self.cur.execute("SELECT 1 FROM paid_invoice WHERE invoice_number = %s;", (inv_number,))
            if self.cur.fetchone():
                print("Ошибка: фактура уже присутствует в paid_invoice.")
                self.conn.rollback()
                return

            self.cur.execute("SELECT iban FROM customer WHERE customer_id = %s;", (customer_id,))
            row = self.cur.fetchone()
            default_iban = row[0] if row else None

            print(f"Оплата: invoice_number={inv_number}, customer_id={customer_id}, amount={amount:.2f}")
            if default_iban is not None:
                print(f"IBAN клиента: {default_iban}")
            pay_iban = input("Введите IBAN для оплаты (оставьте пустым, если хотите использовать IBAN клиента): ")

            if pay_iban == "":
                if default_iban is None:
                    print("IBAN обязателен — у клиента нет IBAN в профиле.")
                    self.conn.rollback()
                    return
                pay_iban = default_iban

            try:
                self.cur.execute(
                    "INSERT INTO paid_invoice (invoice_number, customer_id, amount) VALUES (%s, %s, %s);",
                    (inv_number, customer_id, amount)
                )
                self.cur.execute(
                    "INSERT INTO payment (invoice_number, iban, amount) VALUES (%s, %s, %s);",
                    (inv_number, pay_iban, amount)
                )
                self.cur.execute("DELETE FROM unpaid_invoice WHERE invoice_number = %s;", (inv_number,))

                self.conn.commit()
                print(f"Фактура {inv_number} оплачена: запись в paid_invoice и payment создана, запись удалена из unpaid_invoice.")
            except Exception as e_inner:
                self.conn.rollback()
                print("Ошибка при перемещении фактуры в оплаченные:", e_inner)
        except Exception as e:
            self.conn.rollback()
            print("Ошибка при попытке оплатить фактуру:", e)

    def close(self):
        try:
            if hasattr(self, "cur") and self.cur:
                self.cur.close()
            if hasattr(self, "conn") and self.conn:
                self.conn.close()
        except Exception:
            pass

    def __del__(self):
        self.close()


def main_menu():
    db = DBFacade()
    try:
        while True:
            print("\nДоступные действия:")
            print("1 — Завести клиента")
            print("2 — Завести (создать) НЕоплаченную счет-фактуру (ввести номер вручную)")
            print("3 — Показать список неоплаченных счетов")
            print("4 — Оплатить счет (выбрать из списка неоплаченных)")
            print("6 — Выход")

            choice = input("Ваш выбор: ")
            if choice == '1':
                db.add_client()
            elif choice == '2':
                db.add_unpaid_invoice()
            elif choice == '3':
                db.list_unpaid_invoices()
            elif choice == '4':
                db.pay_invoice()
            elif choice == '5':
                db.search_paid()
            elif choice == '6':
                break
            else:
                print("Неверный ввод.")
    finally:
        db.close()
        print("Соединение с БД закрыто. Пока!")


def run():
    main_menu()

run()
