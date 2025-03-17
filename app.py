import flask

app = flask.Flask(__name__)


@app.route('/')
def hello_world():
    return flask.render_template("template.html", title = "Hello World", text = "Hello World")


if __name__ == '__main__':
    app.run()