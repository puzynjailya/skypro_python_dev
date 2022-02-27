from flask import Flask, request, render_template, send_from_directory
from main.views import main_page
from loader.views import add_post

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024
app.register_blueprint(main_page)
app.register_blueprint(add_post)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

