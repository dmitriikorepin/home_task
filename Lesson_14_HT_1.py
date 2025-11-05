class Product:
    def __init__(self, name, store, price):
        self.__name = name
        self.__store = store
        self.__price = price

    # Методы для доступа к закрытым полям
    def get_name(self):
        return self.__name

    def get_store(self):
        return self.__store

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"{self.__name} | {self.__store} | {self.__price} BYN"


class Warehouse:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def get_by_index(self, index):
        if 0 <= index < len(self.__products):
            return str(self.__products[index])
        return "Product with this index not found."

    def get_by_name(self, name):
        for product in self.__products:
            if product.get_name() == name:
                return str(product)
        return "Product with this name not found."

    def sort_products(self, key="name"):
        if key == "name":
            self.__products.sort(key=Product.get_name)
        elif key == "store":
            self.__products.sort(key=Product.get_store)
        elif key == "price":
            self.__products.sort(key=Product.get_price)
        else:
            raise ValueError("Invalid sort key. Use 'name', 'store', or 'price'.")

    def total_price(self):
        return sum(product.get_price() for product in self.__products)

    def __add__(self, other):
        if isinstance(other, Warehouse):
            total = self.total_price() + other.total_price()
            return f"Total: {total} BYN"
        return NotImplemented

    def __str__(self):
        return "\n".join(str(p) for p in self.__products)


warehouse_one = Warehouse()
warehouse_one.add_product(Product("Bread", "Dana", 50))
warehouse_one.add_product(Product("Milk", "Dana", 80))

warehouse_two = Warehouse()
warehouse_two.add_product(Product("Cheese", "Komarovka", 200))

print("By index:", warehouse_one.get_by_index(0))
print("By name:", warehouse_two.get_by_name("Milk"))

warehouse_one.sort_products("price")
print("After sorting by price:\n", warehouse_one)

print("Total price of two warehouses:", warehouse_one + warehouse_two)