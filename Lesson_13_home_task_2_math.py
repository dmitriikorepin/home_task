class Math:
    # No attributes initialized
    def addition(self, value_a, value_b):
        print(value_a + value_b)

    def subtraction(self, value_a, value_b):
        print(value_a - value_b)

    def multiplication(self, value_a, value_b):
        print(value_a * value_b)

    def division(self, value_a, value_b):
        if value_b != 0:
            print(value_a / value_b)
        else:
            print("Error: Division by zero")

# Get user input
value_a = float(input("Please enter value_a: "))
value_b = float(input("Please enter value_b: "))
action = input("Please enter what needs to be done:\n"
               "1 - addition\n"
               "2 - subtraction\n"
               "3 - multiplication\n"
               "4 - division\n")

# Create Math object
calculator = Math()

# Perform selected action
if action == "1":
    calculator.addition(value_a, value_b)
elif action == "2":
    calculator.subtraction(value_a, value_b)
elif action == "3":
    calculator.multiplication(value_a, value_b)
elif action == "4":
    calculator.division(value_a, value_b)
else:
    print("Invalid action selected")


