from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

# Configura aquí tu clave de Google Gemini
API_KEY = "TU_API_KEY_AQUÍ"
client = genai.Client(api_key=API_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gracias')
def gracias():
    return render_template('gracias.html')

@app.route('/auditar', methods=['POST'])
def auditar():
    data = request.get_json()
    texto_recibido = data.get('texto', '')
    
    if not texto_recibido:
        return jsonify({"resultado": "Error: No se recibió ningún texto."}), 400

    try:
        # Le pedimos a Gemini que actúe como un abogado auditor de prompts
        prompt_para_ia = f"""
        Actúa como un experto en auditoría legal y de prompts de Inteligencia Artificial.
        Analiza el siguiente texto escrito por un usuario. Evalúa si tiene riesgos legales, 
        sesgos, problemas de privacidad o cómo se podría mejorar para que sea más seguro y efectivo.
        
        Texto a auditar:
        "{texto_recibido}"
        
        Devuelve un informe limpio, profesional y bien estructurado en español.
        """

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt_para_ia,
        )
        
        # Guardamos la respuesta real de la IA
        analisis_ia = response.text

    except Exception as e:
        print(f"Error con la API de Gemini: {e}")
        analisis_ia = "Hubo un problema técnico al procesar la auditoría con la IA. Inténtalo de nuevo."

    return jsonify({"resultado": analisis_ia})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
