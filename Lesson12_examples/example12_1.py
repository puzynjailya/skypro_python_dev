from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('form.html')


@app.route('/search')
def search_page():
    search = request.args['s']
    return f'Вы искали слово {search}'

app.run()