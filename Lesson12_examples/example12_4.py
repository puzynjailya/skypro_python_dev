from flask import Flask, request, render_template, send_from_directory


app = Flask(__name__)

@app.route('/uploads/<path:path>')
def static_page(path):
    return send_from_directory('uploads',path)

app.run()