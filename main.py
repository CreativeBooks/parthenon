import uvicorn
from fastapi import FastAPI, HTTPException
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


@app.get("/country/{code}")
def get_country(code: str):
    code = code.lower()
    if code not in Countries:
        raise HTTPException(status_code=404, detail="Country not found")
    return Countries[code]

@app.get("/countries")
def get_countries():
    # return a list of available country codes
    return list(Countries.keys())



if __name__ == "__main__":
        uvicorn.run("main:app", host="127.0.0.1", port=8000)