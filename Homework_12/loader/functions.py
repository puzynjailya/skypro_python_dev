import json
from exceptions import UploadedFileFormatError


def json_decoder(PATH):
    """
    Функция загрузки файла .json
    :param PATH: путь к файлу
    :return: данные из файла, доступные к чтению и изменению
    """
    try:
        with open(PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    # Если ошибка и файл не json, то выдаем ошибку
    except (json.JSONDecodeError, FileNotFoundError):
        return print('Ошибка загрузки файла')


def is_filename_allowed(file_name, extensions_list):
    """
    Функция проверки расширения файла
    :param file_name: имя файла
    :param extensions_list: список доступных расширений
    :return: True - Если расширение доступно для загрузки
    """
    extension = file_name.split(".")[-1]
    if extension in extensions_list:
        return True
    else:
        raise UploadedFileFormatError('Ошибка формата файла')



def is_text_content_valid(content):
    """
    Функция проверки введено контента на валидность
    :param content: введенный контент в формате строки
    :return: True - если контент валидный
    """
    # Проверяем на длину контента, если 0, то пользователь ничего не ввел
    if len(content) != 0:
        # Проверяем на то, не состоит ли текст из одних пробелов
        if len(content.replace(' ', '')) != 0:
            return True


def add_post_to_json(picture, content, json_file):
    """
    Функция добавления данных в файл .json
    :param picture: изображение добавленное пользователем
    :param content: текст, добавленный пользователем
    :param json_file: преобразованный json файл
    :return: данные готовые к загрузке в файл json
    """
    # Проверяем тип данных файла и добавлем новую запись
    if type(json_file) == list:
        json_file.append(dict([('pic', picture), ('content', content)]))
        return json_file
    else:
        print('Ошибка формата файла')


def json_encoder(PATH, updated_file):
    """
    Функция записи нового поста в файл json
    :param PATH: путь к файлу
    :param updated_file: обновленный файл json
    """
    # Открываем файл в режиме записи и обновляем его
    try:
        with open(PATH, 'w', encoding='utf-8') as file:
            json.dump(updated_file, file, ensure_ascii=False)
    # Если ошибка и файл не json, то выдаем ошибку
    except (json.JSONDecodeError, FileNotFoundError):
        return print('Ошибка загрузки файла')
