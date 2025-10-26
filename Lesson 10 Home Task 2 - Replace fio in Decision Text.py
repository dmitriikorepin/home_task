decision = ('Подсудимая Эверт-Колокольцева Елизавета Александровна в судебном '
            'заседании вину инкриминируемого правонарушения признала в полном '
            'объёме и суду показала, что 14 сентября 1876 года, будучи в состоянии '
            'алкогольного опьянения от безысходности, в связи с состоянием здоровья '
            'позвонила со своего стационарного телефона в полицию, сообщив о том '
            'что у неё в квартире якобы заложена бомба. После чего приехали '
            'сотрудники полиции, скорая и пожарные, которым она сообщила, что '
            'бомба это она.')

sentences = decision.split('.')
processed_sentences = []

for sentence in sentences:
    words = sentence.split()
    capitalized = [word for word in words if word[0].isupper()]

    if len(capitalized) == 4:
        if any('-' in word for word in capitalized):
            for word in capitalized[1:]:
                fio = ' '.join(capitalized[1:])
                sentence = sentence.replace(fio, 'N')

    elif len(capitalized) == 3:
        for word in capitalized:
            fio = ' '.join(capitalized[1:])
            sentence = sentence.replace(fio, 'N')

    processed_sentences.append(sentence.strip())

final_text = '. '.join(processed_sentences) + '.'
print(final_text)