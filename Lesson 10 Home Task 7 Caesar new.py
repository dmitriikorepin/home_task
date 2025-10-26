"""
Implement one functions: encrypts a given file using the Caesar cipher
"""
def caeser_function(some_text, param_step):
    alph_eng_big = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alph_eng_small = list("abcdefghijklmnopqrstuvwxyz")
    alph_rus_big = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
    alph_rus_small = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    result = ""

    for i in some_text:
        if i in alph_eng_big:
            index = alph_eng_big.index(i)
            new_index = index + param_step
            result += alph_eng_big[new_index % len(alph_eng_big)] # учитываем граничное условие

        elif i in alph_eng_small:
            index = alph_eng_small.index(i)
            new_index = index + param_step
            result += alph_eng_small[new_index % len(alph_eng_small)]

        elif i in alph_rus_big:
            index = alph_rus_big.index(i)
            new_index = index + param_step
            result += alph_rus_big[new_index % len(alph_rus_big)]

        elif i in alph_rus_small:
            index = alph_rus_small.index(i)
            new_index = index + param_step
            result += alph_rus_small[new_index % len(alph_rus_small)]

        else:
            result += i

    return result

with open('Data4Caeser.txt', 'r') as my_file:
    line_number = 1
    for line in my_file:
        some_text = line.strip()
        param_step = line_number
        result = caeser_function(some_text, param_step)
        print(f"Строка {line_number} (сдвиг {param_step}): {result}")
        line_number += 1


