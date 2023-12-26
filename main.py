from flask import Flask, request
from noticias import Peticion

app = Flask(__name__)

@app.route("/api")
def api():
    p = Peticion()
    news = p.getDatos()
    return news

@app.route("/api/noticias", methods=["POST"])
def noticias():
    peticion = request.get_json()

    p = Peticion(q=peticion["texto"])

    news = p.getDatos()

    return news

if __name__ == "__main__":
    app.run()