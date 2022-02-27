from flask import Flask, render_template
from utils import *

# Определяем путь к файлу с нашими данными
PATH = 'candidates.json'

# Создаем экземпляр фласка
app = Flask(__name__)

# Загружаем файл с данными на кандидатов
candidates = load_candidate_from_json(PATH)


# Создаем заглавную страницу
@app.route('/')
def index_page():
    return render_template('list.html', candidates=candidates)


# Создаем страницу поиска по ID
@app.route('/candidate/<int:candidate_id>/')
def candidate_page(candidate_id):
    candidate = get_candidate(candidates, candidate_id)
    return render_template('card.html', candidate=candidate)


# Создаем страницу поиска по имени
@app.route('/search/<candidate_name>/')
def search_by_name_page(candidate_name):
    candidate_list = get_candidate_by_name(candidates, candidate_name)
    return render_template('search.html',
                           candidates=candidate_list,
                           length=len(candidate_list),
                           search=candidate_name)


# Создаем страницу поиска по навыку
@app.route('/skill/<skill_name>/')
def skill_page(skill_name):
    candidate_list = candidates_by_skill(candidates, skill_name, limit=2)
    return render_template('skill.html',
                           candidates=candidate_list,
                           length=len(candidate_list),
                           skill=skill_name)


app.run(port=5000)
