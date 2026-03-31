"""
TP simplifie — FastAPI + Hugging Face
But: remplacer uniquement les TODO_REPLACE.
"""

import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# TODO_REPLACE_0:
# - Importer load_dotenv depuis dotenv
# - Importer requests
# - Appeler load_dotenv() une seule fois au demarrage
# HINT:
# from dotenv import load_dotenv
# import requests
# load_dotenv()

app = FastAPI(title="TP Hugging Face", version="0.1")

# TODO_REPLACE_1: URL du routeur HF
HF_URL = None
# HINT:
# HF_URL = "https://router.huggingface.co/v1/chat/completions"

# TODO_REPLACE_2: modele HF
HF_MODEL = None
# HINT:
# HF_MODEL = "meta-llama/Llama-3.2-1B-Instruct"


class GenerateRequest(BaseModel):
    # TODO_REPLACE_3:
    # - Renommer le champ en prompt
    # - Garder min_length=1
    # HINT:
    # prompt: str = Field(..., min_length=1, alias="prompt")
    a_remplacer: str = Field(..., min_length=1, alias="prompt")


def get_hf_token():
    # TODO_REPLACE_4:
    # Lire HUGGINGFACE_API_KEY, strip, retourner None si vide
    # HINT (reponse possible):
    # key = os.getenv("HUGGINGFACE_API_KEY")
    # if key:
    #     key = key.strip()
    # if not key:
    #     return None
    # return key
    return None


@app.get("/health")
def health():
    # HINT (reponse possible):
    # token = get_hf_token()
    # return {
    #     "status": "ok" if token else "degraded",
    #     "huggingface_configured": bool(token),
    # }
    token = get_hf_token()
    return {
        "status": "ok" if token else "degraded",
        "huggingface_configured": bool(token),
    }


@app.post("/generate")
def generate(body: GenerateRequest):
    # TODO_REPLACE_5:
    # HINT (reponse possible complete):
    # 1) verifier token:
    # token = get_hf_token()
    # if not token: raise HTTPException(503, ...)
    #
    # 2) construire headers + payload:
    # headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    # payload = {"model": HF_MODEL, "messages":[{"role":"user","content": body.prompt}], "max_tokens":128}
    #
    # 3) appel HTTP:
    # resp = requests.post(HF_URL, headers=headers, json=payload, timeout=60)
    #
    # 4) verifier status:
    # if resp.status_code != 200: raise HTTPException(502, ...)
    #
    # 5) parser reponse:
    # data = resp.json()
    # text = data["choices"][0]["message"]["content"].strip()
    #
    # 6) retourner:
    # model_short = HF_MODEL.rsplit("/", 1)[-1]
    # return {"text": text, "model": model_short}
    raise HTTPException(
        status_code=501,
        detail="TP: complete TODO_REPLACE_5 dans generate().",
    )
