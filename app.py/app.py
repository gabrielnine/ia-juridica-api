from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    modelo, vectorizer = pickle.load(f)

@app.route("/prever", methods=["POST"])
def prever():
    texto = request.json["texto"]
    texto_vetorizado = vectorizer.transform([texto])
    resultado = modelo.predict(texto_vetorizado)[0]
    return jsonify({"classe": resultado})

app.run(debug=True)