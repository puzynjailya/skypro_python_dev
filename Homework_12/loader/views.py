from flask import Blueprint, request, render_template  # Подключаем фласк
from .functions import *  # Подключаем модуль с вспомогательными функциями
from werkzeug.utils import secure_filename  # Подключаем для использования защищенного имени
import os  # Подключаем os для работы с файлами
from exceptions import UploadedFileFormatError  # Подключаем модуль искючений
import logging  # Подключаем логирование

# Создаем блюпринт
add_post = Blueprint('add_page', __name__,
                     template_folder='templates')

# Задаем конфигурацию логирования и создаем файл, в который будем записывать логи
logging.basicConfig(filename='add_post.log', level=logging.INFO)

# Создаем список допустимых форматов файла изображения
extensions_list = ['png', 'jpg', 'jpeg', 'gif']


# Создаем страницу /post/ с методом GET для отображения формы добавления поста
@add_post.route('/post/', methods=['GET'])
def add_new_post():
    return render_template('post_form.html')


# Создаем страницу /post/ с методом POST для загрузки данных из формы добавления поста
@add_post.route('/post', methods=['POST'])
def add_page():
    # Задаем путь к файлу json
    PATH = './posts.json'

    # Получаем картинку и текст
    picture = request.files.get('picture')
    post_text = request.form['content']

    # Если пользователь не ввел текст или не добавил файл для загрузки, то выводим страницу ошибку
    if not picture or not is_text_content_valid(post_text):
        # Логируем ошибку
        logging.exception('Ошибка при загрузке файла. Не добавлен файл или текст')
        return render_template('content_error.html')

    try:
        # Сохраняем имя файла с защищенном формате
        picture_name = secure_filename(picture.filename)
        # Создаем путь к файлу
        picture_path = os.path.join('./uploads/images/', picture_name)

        # Если разрешение файла и текст валидные:
        if is_filename_allowed(picture_name, extensions_list) and is_text_content_valid(post_text):
            # Сохраняем файл с картинкой
            picture.save(picture_path)
            # Открываем файл json
            json_file = json_decoder(PATH)
            # Добавляем данные поста в декодированный файл
            updated_json = add_post_to_json(picture_path[1:], post_text, json_file)
            # Сохраняем файл json
            json_encoder(PATH, updated_json)
            return render_template('post_uploaded.html', post_text=post_text, picture_path=picture_path[1:])

    # При возникновении ошибки по формату файла:
    except UploadedFileFormatError:
        # Логируем данные
        logging.info(f'Загружаемый файл имеет неверное расширение и не картинка - {picture.filename}')
        return render_template('filename_error.html', filename=picture_name)

    except FileNotFoundError:
        return 'Ошибка при сохранении файла. Неверный путь. Обратитесь за поддержкой куда-то!'


# Задаем действия при очень большом файле
@add_post.errorhandler(413)
def page_not_found(e):
    return "<h1>Файл большеват</h1><p>Поищите поменьше, плиз!</p>", 413
