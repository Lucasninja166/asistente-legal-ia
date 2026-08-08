from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/procesar", methods=["POST"])
def procesar():
    datos = request.get_json()
    texto = datos.get("texto", "")

    # Acá va tu motor de datos/procesamiento
    resultado = texto.upper()

    return jsonify({
        "resultado": resultado
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
