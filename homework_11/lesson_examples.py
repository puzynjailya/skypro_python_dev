from flask import Flask, request, render_template

app_new = Flask(__name__)


@app_new.route('/')
def page_index():
    page_content = """
        <h1>Здоров чувачок!</h1>
        <p>Ты написал первую страницу</p>
        <p>Ну и как же без Hello world!</p>
        <a href="link"> Ссылка в никуда </a>        
    """
    return page_content

@app_new.route('/link/')
def page_link():
    page_content = """<!DOCTYPE html>
    <html>
        <head>
            <meta charset = 'UTF-8'>
            <title>Дичь какая-то</title>
        </head>
        <body>
            <p>А тут еще большая дичь!</p>
        </body>
    </html>
    """
    return page_content


app_new.run(port=5001)
