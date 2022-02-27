import json


def load_candidate_from_json(PATH):
    """
    Функция для открытия json файла
    :param PATH: путь к файлу
    :return: преобразованный файл json
    """
    with open(PATH, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_candidate(candidates, candidate_id):
    """
    Функция, которая получает данные кандидата по его id
    :param candidates: list - распарсенный файл кандидатов
    :param candidate_id: int - значение поля id кандидата
    :return: data: dict - возвращает данные по кандидату в формате словаря
    """
    for data in candidates:
        if data.get('id') == candidate_id:
            return data


def get_candidate_by_name(candidates, candidate_name):
    """
    Функция получения списка кандидатов по имени кандидата
    :param candidates: list - распарсенный файл кандидатов
    :param candidate_name: str - поисковый запрос
    :return: data: dict - возвращает список кандидатов содержащих заданный параметр для поиска
    """
    output_list = []
    for data in candidates:
        # Если поисковый запрос находится в имени пользователя, то добавляем его в выходной список
        if candidate_name.lower() in data.get('name').lower():
            output_list.append(data)
    return output_list


def candidates_by_skill(candidates, skill_name, limit=False):
    """
    Функция получения отформатированного списка данных кандидата, для которого в навыках есть skills
    :param candidates: list - распарсенный файл кандидатов
    :param skill_name: str - имя навыки
    :param limit: int - Задает количество выводимых данных (по умолчанию False)
    :return:
    """
    # Небольшой анализ данных json файла показал, что файл содержит перечисление навыков, при этом
    # Навыки могут быть как написаны по-русски, так и по-английски, могут быть через запятую, а могут быть и нет
    # Могут быть с большой буквы, а могут быть и нет, поэтому необходимо учесть эти моменты

    # Создаем пустой список для вывода данных
    output_list = []

    # Пройдемся по каждой хеш-таблице и проверим есть ли в ней искомый навых
    for data in candidates:
        # В условии сразу учитывается нижний регистр для искомого skill_name и skills
        # Используем set, чтобы немного ускорить поиск и не искать среди дублей
        if skill_name.lower() in set(data['skills'].lower().split(', ')):
            output_list.append(data)
    if limit:
        return output_list[:limit]
    else:
        return output_list
