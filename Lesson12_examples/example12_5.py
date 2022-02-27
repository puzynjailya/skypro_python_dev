from flask import Flask, request, render_template

# Импортируем блюпринты из их пакетов
from category.views import catalog_blueprint


app = Flask(__name__)

# Регистрируем первый блюпринт
app.register_blueprint(catalog_blueprint)

app.run()
