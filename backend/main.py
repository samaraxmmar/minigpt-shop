from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from langchain_ibm import WatsonxLLM
import os

# Chargement des variables d'environnement Watsonx
os.environ["WATSONX_APIKEY"] = "WUmCVnhYhqKGT6Ga8dDXhOgy74Q9woCIE7tKa7mQy3oB"

# Paramètres du modèle
parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 500
}

# Instanciation du LLM Watsonx
llm = WatsonxLLM(
    model_id="meta-llama/llama-3-3-70b-instruct",
    url="https://us-south.ml.cloud.ibm.com",
    params=parameters,
    project_id="871d5c7f-bb96-49d8-a197-6678e0abd16b",
)

# Initialisation FastAPI
app = FastAPI(title="MiniGPT-Shop API", version="1.0.0")

# Activation du CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En prod : remplace "*" par l’URL de ton frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schémas Pydantic
class ChatMessage(BaseModel):
    message: str
    user_id: Optional[str] = "anonymous"

class ChatResponse(BaseModel):
    response: str
    timestamp: str

# Route principale
@app.get("/")
async def root():
    return {"message": "MiniGPT-Shop API is running!"}

# Route chat POST
@app.post("/chat", response_model=ChatResponse)
async def chat_with_ai(message: ChatMessage):
    try:
        response = llm.invoke(message.message)
        return ChatResponse(
            response=response,
            timestamp=datetime.now().isoformat()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'appel au modèle IA : {e}")

# (Optionnel) Ajout manuel pour préflight OPTIONS si le navigateur bloque
@app.options("/chat")
async def options_chat():
    return {"status": "OK"}

# Démarrage
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
