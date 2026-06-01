from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
SEARXNG = "http://localhost:10000"

@app.route("/search")
def search():
    q = request.args.get("q", "")
    fmt = request.args.get("format", "json")
    r = requests.get(f"{SEARXNG}/search", params={
        "q": q, "format": fmt, "pageno": 1, "language": "en"
    }, headers={"User-Agent": "Mozilla/5.0"})
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)





"""
import httpx
import asyncio
from fastapi import FastAPI, Response
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows your Netlify URL to connect
    allow_credentials=False,
    allow_methods=["*"],  # Resolves the 405 OPTIONS error
    allow_headers=["*"],
)

@app.post("/")
def health_responder():
    return {"response":"Healthy"}

class Input(BaseModel):
    model: str
    temperature: float = 0.5
    prompt: str
    change: bool = True
    Models: Optional[list] = None


@app.post("/connector")
async def connector_load_balancer(inputs:Input):
    load_balancer_uri = "https://npmaiecosystem-loadbalancer.hf.space/load_balancer"
    load_balancer_fall_uri = "https://npmaiecosystem-loadbalancerfallback.hf.space/load_balancer"

    payload = {
        "model":inputs.model,
        "temperature":inputs.temperature,
        "prompt":inputs.prompt,
        "change":True,
        "Models":inputs.Models
    }

    timeout = httpx.Timeout(connect=100.0, read=560.0, write=300.0, pool=320.0)

    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(load_balancer_uri, json=payload)
            response.raise_for_status()
            f_response = response.json()["response"]
            return {"response":f_response}
            
    except Exception as e:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(load_balancer_fall_uri, json=payload)
            response.raise_for_status()
            f_response_f = response.json()["response"]
            return {"response":f_response_f}
"""
