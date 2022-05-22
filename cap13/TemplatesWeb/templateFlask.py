from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)


@app.route("/")
def menu():
    return render_template('template.html')


@app.route("/hello/<string:usuario>/")
def menuHello(usuario):
    return render_template('templateHello.html', usuario=usuario)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
