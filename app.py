import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI  # Formato moderno de la biblioteca oficial

app = FastAPI()

# Permiso obligatorio de seguridad (CORS) para conectar con tu HTML
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializamos el cliente moderno de OpenAI
# Nota: En producción, lo ideal es dejar los paréntesis vacíos () 
# y que Python lea la clave de forma oculta desde el servidor.
client = OpenAI(api_key="TU_LLAVE_SECRETA_DE_OPENAI")

class ContratoEntrada(BaseModel):
    texto: str

@app.post("/analizar-contrato")
async def analizar_documento(contrato: ContratoEntrada):
    try:
        # Petición oficial y protocolar a los servidores de ChatGPT
        respuesta = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system", 
                    "content": "Eres un abogado experto en auditoría de contratos. Tu tarea es encontrar las 3 cláusulas más riesgosas o abusivas y explicarlas de forma súper simple."
                },
                {
                    "role": "user", 
                    "content": f"Analiza este contrato:\n\n{contrato.texto}"
                }
            ]
        )
        # Devolvemos el resultado real generado por la IA
        return {"analisis": respuesta.choices.message.content}
        
    except Exception as e:
        # Si la clave es de ejemplo, nos avisará con el código de error correspondiente
        raise HTTPException(status_code=500, detail=str(e))