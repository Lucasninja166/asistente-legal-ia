import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContratoEntrada(BaseModel):
    texto: str

# Acá ya tiene puesta la barra final exacta que necesita Render
@app.post("/analizar-contrato/")
async def analizar_documento(contrato: ContratoEntrada):
    texto_usuario = contrato.texto.lower()
    
    if "perro" in texto_usuario or "chocolates" in texto_usuario or "croquetas" in texto_usuario:
        analisis_simulado = (
            "⚠️ ANÁLISIS DE RIESGO LEGAL (SIMULACIÓN GRATUITA):\n\n"
            "1. CLÁUSULA ABUSIVA DETECTADA: Se identifica una transferencia forzosa de bienes "
            "(chocolates/croquetas) hacia un tercero de cuatro patas ('El Perro').\n\n"
            "2. RIESGO DE SALUD: El chocolate es altamente tóxico para los caninos. "
            "Esta cláusula es nula de pleno derecho por poner en riesgo la vida del sujeto beneficiario.\n\n"
            "3. RECOMENDACIÓN: Reemplazar los chocolates por caricias o paseos en el parque inmediatamente."
        )
    else:
        analisis_simulado = f"Documento recibido con éxito en la nube: '{contrato.texto}'. ¡Tu sistema gratis funciona perfecto!"
        
    return {"analisis": analisis_simulado}
  
