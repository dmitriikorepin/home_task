import re

def underachiever(filename):
    with open(filename, 'r') as my_file:
        content_lines = my_file.readlines()
        is_found = False
        for student in content_lines:
            student = student.strip()
            if student[-1].isdigit() and int(student[-1]) < 3:
                print(student)
                is_found = True
        if is_found == False:
            print("There are no underachievers")

underachiever('underachiever.txt')
