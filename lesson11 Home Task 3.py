with open ("data.txt", "r") as my_file:
    data = my_file.readlines()
# сырые данные
    data = list(map(lambda x: x.replace("\n", ""), data))
# Кадлуб строку разбить на слова
# окажем кажду строку со списком слов
    out_data = []

    for row in data:
        frequencies = {}
        words = row.split(" ")
        for word in words:
            frequencies[word] = row.count(word)
        min_freq = min(frequencies.values())
        max_freq = max(frequencies.values())
# если максимм и минимум совпали то значит один раз встречается
        if min_freq == max_freq:
            out_data.append("equal counts\n")
        # {} - словарь - карта соотвествия сколько раз оно встртилост
        else:
            for word, freq in frequencies.items():
                if freq == max_freq:
                    out_data.append(f"{freq}: {word}\n")

    print(out_data)

    with open("result", "w") as res_file:
        res_file.writelines(out_data)
