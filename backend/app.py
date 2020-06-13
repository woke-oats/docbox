from flask import Flask, render_template
import sqlite3

app = Flask(__name__, template_folder="templates")
conn = sqlite3.connect("text.db")


@app.route("/")
def index():
    # app.send_static_file('index.html')
    return "hello"


if __name__ == "__main__":
    app.run()
