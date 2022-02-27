from flask import Blueprint, request, render_template
from . import functions
import logging

main_page = Blueprint('main_page',
                      __name__,
                      template_folder='templates')

# Задаем конфигурацию логирования и создаем файл, в который будем записывать логи
logging.basicConfig(filename='add_post.log', level=logging.INFO, encoding='windows-1251')


# Создаем заглавную страницу
@main_page.route('/')
def index_page():
    return render_template('index.html')


# Создаем страницу поиска
@main_page.route('/search/')
def search_page():
    # Открываем файл json
    decoded_json = functions.json_decoder('./posts.json')
    # Получаем данные из запроса
    target = request.args['s']
    # Проверяем совпадение текста постов и искомых слов
    match_list = functions.target_search(decoded_json, target)
    # Логируем наш поиск
    logging.info(f'Выполнен поиск по запросу {target}')
    return render_template('post_list.html', target=target, match_list=match_list)
