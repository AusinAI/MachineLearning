from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def research():
    return {"Hello":"World"}
