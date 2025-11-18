class Bus:
    def __init__(self, max_speed, max_seats):
        self.speed = 0
        self.max_speed = max_speed
        self.max_seats = max_seats
        self.passengers = []
        self.has_free_seats = True
        self.seats_map = {}

    def update_has_free_seats_flag(self):
        self.has_free_seats = len(self.passengers) < self.max_seats

    def board_passenger(self, *names):
        for name in names:
            if len(self.passengers) < self.max_seats:
                self.passengers.append(name)
                seat_number = len(self.passengers)
                self.seats_map[seat_number] = name
            else:
                print(f"Нет свободных мест для {name}")
        self.update_has_free_seats_flag()

    def unboard_passenger(self, *names):
        for name in names:
            if name in self.passengers:
                self.passengers.remove(name)
                # удалить из словаря мест
                for seat, passenger in list(self.seats_map.items()):
                    if passenger == name:
                        del self.seats_map[seat]
            else:
                print(f"{name} не найден в автобусе")
        self.update_has_free_seats_flag()

    def change_speed(self, delta):
        new_speed = self.speed + delta
        if new_speed < 0:
            self.speed = 0
        elif new_speed > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed = new_speed

    # Операция in
    def __contains__(self, name):
        return name in self.passengers

    # Операция += (посадка)
    def __iadd__(self, name):
        self.board_passenger(name)
        return self

    # Операция -= (высадка)
    def __isub__(self, name):
        self.unboard_passenger(name)
        return self

    def __str__(self):
        return (f"Скорость: {self.speed}, Пассажиры: {self.passengers}, "
                f"Свободные места: {self.has_free_seats}, Места: {self.seats_map}")

bus = Bus(max_speed=120, max_seats=3)
bus.board_passenger("Иванов", "Петров")
bus.unboard_passenger("Петров")
bus.change_speed(50)
print("Иванов" in bus)

bus += "Сидоров"
bus -= "Иванов"
print(bus)