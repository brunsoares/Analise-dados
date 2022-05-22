from flask import Flask

app = Flask(__name__)


@app.route("/")     # Main


def helloWorld():
    return "Hello World com Flask"


if __name__ == "__main__":      # Se estiver na main, rodará o aplicativo
    app.run()
