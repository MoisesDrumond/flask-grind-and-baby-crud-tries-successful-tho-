from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "index"

@app.route("/teste")
def teste():
    return "Teste"

if __name__ == '__main__':
    app.run()
