import shutil

from PIL import Image
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/resizeimage',methods=["POST"])
def teste():
    obj = request.get_json()

    nomearquivo = obj.get("nome")
    urlentrada = obj.get("entrada")
    urlsaida = obj.get("saida")
    tipo = obj.get("tipo")

    if(tipo == 0):
        originalName = nomearquivo.split(".")
        image = Image.open(urlentrada + "\\" + nomearquivo)
        new_image = image.resize((400, 400))
        new_image.save(urlsaida + "\\" + nomearquivo)
    else:
        shutil.copy(urlentrada + "\\" + nomearquivo,urlsaida + "\\" + nomearquivo)

    return 'DEU Boa'

if __name__ == '__main__':
    app.run()
