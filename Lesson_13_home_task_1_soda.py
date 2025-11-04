class Soda:
    def __init__(self, flavor=None):
        self.flavor = flavor

    def __str__(self):
        if self.flavor:
            return f'your limonade has <{self.flavor}> flavor'
        else:
            return 'You have no flavor'

limonade = Soda(input("Please enter a flavor: "))
print(limonade)