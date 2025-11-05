class Beeelephant:
    def __init__(self, part_one_bee, part_two_elephant):
        self.bee = max(0, min(100, part_one_bee))
        self.elephant = max(0, min(100, part_two_elephant))

    def fly(self):
        return self.bee >= self.elephant

    def trumpet(self):
        return "tu-tu-doo-doo" if self.elephant >= self.bee else "wzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.bee = min(100, self.bee + value)
            self.elephant = max(0, self.elephant - value)
        elif meal == "grass":
            self.elephant = min(100, self.elephant + value)
            self.bee = max(0, self.bee - value)