from fastapi import FastAPI

app = FastAPI(
    title= "Mi primera API",
    description="Aprendiendo FastAPI",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {"message":"¡Hi,FastAPI!"}

