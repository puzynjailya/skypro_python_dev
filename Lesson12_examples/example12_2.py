from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def form_page():
    form_content = """
    <h2>Форма добавления какой-то задачи</h2>
    <form action ='/add' method='post'>
    <input type = "text" name = 'task_name'>
    <input type = "submit" value = 'Добавить'>
	</form>
	"""
    return form_content


@app.route('/add', methods=["POST"])
def add_page():
    task = request.form['task_name']
    return f'Вы добавили задачу {task}'

@app.route("/test", methods=['GET', "POST"])
def test_page():
    name = request.values.get('name')
    return f"Вы ввели имя {name}"

app.run()
