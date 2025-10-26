import json
import csv
import os
import re

new_employee = None

def convert_json_to_csv():
    with open('employees.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    with open('output.csv', 'w', newline='', encoding='utf-8') as csv_file:
        field_names = ["name", "birthday", "height", "weight", "car", "languages"]
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    print("JSON data has been successfully converted to CSV.")

def create_new_employee():
    name = input("Enter employee name: ")
    birthday = input("Enter birthday: ")
    height = input("Enter height: ")
    weight = input("Enter weight: ")
    car = input("Does the employee have a car? (1 - Yes, 0 - No): ")
    car = car == "1"
    languages = input("Enter languages (comma-separated): ").split(',')
    languages = [lang.strip() for lang in languages]

    return {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": languages
    }

def add_employee_to_csv(employee):
    employee["languages"] = ", ".join(employee["languages"])
    file_exists = os.path.isfile('employees.csv')

    with open('employees.csv', 'a', newline='', encoding='utf-8') as csv_file:
        field_names = ["name", "birthday", "height", "weight", "car", "languages"]
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        if not file_exists:
            writer.writeheader()
        writer.writerow(employee)

    print("Employee has been added to CSV.")




def show_employee_details():
    name = input("Enter the name of the employee to search: ")
    try:
        with open('employees.json', 'r', encoding='utf-8') as json_file:
            employees = json.load(json_file)

        for employee in employees:
            if employee["name"].lower() == name.lower():
                print("\nEmployee details:")
                print(f"Name: {employee['name']}")
                print(f"Birthday: {employee['birthday']}")
                print(f"Height: {employee['height']}")
                print(f"Weight: {employee['weight']}")
                print(f"Has a car: {'Yes' if employee['car'] else 'No'}")
                print(f"Languages: {', '.join(employee['languages'])}")
                return
        print("Employee not found.")

    except FileNotFoundError:
        print("The employees.json file was not found.")




def my_language_employees_filter():
    my_language = input("Enter a language to search for: ").strip()
    try:
        with open('employees.json', 'r', encoding='utf-8') as json_file:
            employees = json.load(json_file)

        pattern = re.compile(my_language, re.IGNORECASE)
        found = False

        for employee in employees:
            if any(pattern.search(lang) for lang in employee["languages"]):
                print("\nEmployee details:")
                print(f"Name: {employee['name']}")
                print(f"Birthday: {employee['birthday']}")
                print(f"Height: {employee['height']}")
                print(f"Weight: {employee['weight']}")
                print(f"Has a car: {'Yes' if employee['car'] else 'No'}")
                print(f"Languages: {', '.join(employee['languages'])}")
                found = True

        if not found:
            print(f"No employees found with language matching: {my_language}")

    except FileNotFoundError:
        print("The employees.json file was not found.")




def my_filter_by_birth_y_and_av_height():
    try:
        year_input = int(input("Enter a birth year YYYY: "))
        with open('employees.json', 'r', encoding='utf-8') as json_file:
            employees = json.load(json_file)

        heights = []
        for employee in employees:
            try:
                birth_year = int(employee['birthday'].split('.')[-1])
                if birth_year < year_input:
                    heights.append(float(employee['height']))
            except (ValueError, IndexError):
                continue

        if heights:
            average_height = sum(heights) / len(heights)
            print(f"Average height of employees born before {year_input}: {average_height}")
        else:
            print(f"No employees found born before {year_input}.")

    except ValueError:
        print("Invalid year input. Please enter a valid number.")
    except FileNotFoundError:
        print("The employees.json file was not found.")



# Initialize JSON file if missing
try:
    with open('employees.json', 'r', encoding='utf-8') as json_file:
        employees = json.load(json_file)
except (FileNotFoundError, json.JSONDecodeError):
    employees = []
    with open("employees.json", 'w', encoding='utf-8') as json_file:
        json.dump(employees, json_file, ensure_ascii=False, indent=4)
    print("Initialized empty employee list.")

# Main loop
while True:
    print("\nWhat would you like to do?")
    print("1 - Convert JSON to CSV")
    print("2 - Create a new employee and save to JSON")
    print("3 - Add the last created employee to CSV")
    print("4 - Show employee details by name")
    print("5 - Show employee details by language")
    print("6 - Show employee details by birth year")
    print("0 - Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        convert_json_to_csv()

    elif choice == "2":
        new_employee = create_new_employee()
        employees.append(new_employee)
        with open("employees.json", 'w', encoding='utf-8') as json_file:
            json.dump(employees, json_file, ensure_ascii=False, indent=4)
        print("Employee has been saved to JSON.")

    elif choice == "3":
        if new_employee:
            add_employee_to_csv(new_employee)
        else:
            print("No employee has been created yet. Please create one first.")

    elif choice == "4":
        show_employee_details()

    elif choice == "5":
        my_language_employees_filter()

    elif choice == "6":
        my_filter_by_birth_y_and_av_height()

    elif choice == "0":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")