main_str = '''
          Данное предложение будет разбиваться на отдельные слова.
          В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов.
          Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
'''

alphabet = ('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
            'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я')

split_main_str = main_str.split(' ')
split_main_str = list(filter(None, split_main_str))

new_main_str = []
for letter in alphabet:
    for word in split_main_str:
        if word[0].lower() == letter:
            new_main_str.append(word.lower())

main_str = ' '.join(new_main_str)

def get_count_char(main_str):
    dic = {}
    for word in main_str:
        for index in range(len(word)):
            if word[index].isalpha() == True:
                if word[index] in dic:
                    dic[word[index]] += 1
                else:
                    dic.update({word[index]: 1})

    return dic

def percent(dic, main_str):
    new_dic = {}
    sum_main_str = len(main_str)
    for key, value in dic.items():
        new_dic.update({key:(value*100)/sum_main_str})

    return new_dic
