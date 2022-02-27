from flask import Flask, render_template, request

app = Flask(__name__)
# Ограничиваем размер файла здесь 2 Мб (2 *1024*1024)
app.config['MAX_CONTENT_LENGTH'] = 2 * 2**10 * 2**10

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


# Создаем функцию проверки расширения файла
def is_file_allowed(filename_):
    global extension
    extension = filename_.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    else:
        return False


@app.route('/')
def index_page():
    return render_template('upload_form.html')


@app.route('/upload', methods=["POST"])
def upload_page():
    """ Эта вьюшка обрабатывает форму, вытаскивает из запроса файл и показывает его имя"""
    # Получаем объект картинки из формы
    picture = request.files.get('picture')
    filename_ = picture.filename
    if is_file_allowed(filename_):
        picture.save(f'./uploads/{filename_}')
        return f'Загружен файл {picture.filename}'
    else:
        return f'Неверное расширение. Расширение {extension} не поддерживается'

@app.errorhandler(413)
def file_size_error(e):
    return "<h1>Файл большеват</h1><p>Поищите поменьше, плиз!</p>", 413


app.run()
