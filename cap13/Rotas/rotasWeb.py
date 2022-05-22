from flask import Flask

app = Flask(__name__)


@app.route("/")
def rotaMain():
    return "Você está na rota Main < / >"


@app.route("/hello")
def rotaHello():
    return "Você está na rota Hello < /hello >"


@app.route("/usuario")
def rotaUsuario():
    return "Você está na rota Usuario < /usuario >"


@app.route("/usuario/<string:usuario>/")        # Pegando parametros da URL
def getUsuario(usuario):
    return "Você é "+usuario+" e está na rota de Usuario < /usuario/"+usuario+" >"


if __name__ == "__main__":
    app.run()
