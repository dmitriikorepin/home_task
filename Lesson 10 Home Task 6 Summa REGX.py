import re

def my_summ(filename):
    summ = 0
    with open(filename, 'r', encoding='utf-8') as my_file:
        content = my_file.read()
        numbers = re.findall(r'\d+', content)
        for num in numbers:
            summ += int(num)
        print(summ)


my_summ('Lesson10_Home_Task_6.txt')