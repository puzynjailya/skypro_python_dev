import json


def json_decoder(PATH):
    try:
        with open(PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return f'Ошибка загрузки файла'


def target_search(json_decoded, target):
    # Разделяем, если юзер ввел несколько слов через пробел
    target = target.replace(',',' ').split(' ')
    # Создаем пустой список, куда будем складывать слова
    match_list = []
    for word in target:
        for data in json_decoded:
            if word.lower() in data.get('content').lower():
                match_list.append(data)
    return match_list


