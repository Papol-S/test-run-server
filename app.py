from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return "hello world"


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=80)
