from flask import flask, jsonify
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

Countries = {
    "japan": {
        "name": "Japan",
        "capital": "Tokyo",
        "language": "Japanese",
    }
}

@app.get("/countries")
def get_countries():
    # return a list of available country codes
    return Countries

