import re

def my_file_censore(my_file_text, stop_words):

    with open('stop_words.txt', 'r', encoding='utf-8') as stop_words_file:
        stop_words = stop_words_file.read().split()
        print(f" STOP WORDS: {stop_words}")

    with open ('input.text.txt', 'r', encoding='utf-8') as my_file:
        my_file_text = my_file.read()
    print(f" INITIAL TEXT: {my_file_text}")

    for word in stop_words:
        pattern = re.compile(re.escape(word),re.IGNORECASE)  # re.escape("exam.")  # returns 'exam\\.' it is needed for special symbols
        my_file_text = pattern.sub('*' * len(word), my_file_text)  # create a string *** with the same length as word has
    print(f" CENSORED TEXT: {my_file_text}")
    return my_file_text

censored_text = my_file_censore('input.text.txt', 'stop_words.txt')