import sqlite3

from flask import Flask, jsonify, render_template, request, url_for

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/display/<number>")
def display(number):
    conn = sqlite3.connect("text.db")
    cursor = conn.cursor()
    text = (
        conn.execute("SELECT doc FROM documents WHERE rowid=?", (number,))
        .fetchone()[0]
        .decode()[1:-1]
    )
    return render_template("display.html", text=text)


@app.route("/create", methods=["POST"])
def create():
    """ Creates new entry in database for text """
    conn = sqlite3.connect("text.db")
    cursor = conn.cursor()
    data = request.data

    # check for max input size
    if len(data) > 1000000:
        return jsonify({"url": "error: text too long"})
    cursor.execute("INSERT INTO documents (doc) VALUES (?)", (data,))
    conn.commit()
    rowid = cursor.lastrowid

    return jsonify(
        {
            "url": "{}{}".format(
                request.base_url.replace("create", "")[:-1],
                url_for("display", number=rowid),
            )
        }
    )


if __name__ == "__main__":
    app.run()
