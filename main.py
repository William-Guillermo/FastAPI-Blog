from fastapi import FastAPI

app = FastAPI(
    title= "Mi primera API",
    description="Aprendiendo FastAPI",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {"message":"¡Hi,FastAPI!"}

# Endpoint Get 
@app.get("/items/")
async def read_items():
    return [{"name":"Item1"}, {"name":"Item2"}]

# Endpoint Get con ID
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}

# Endpoint POST
@app.post("/items/")
async def create_item(name: str):
    return {"name" :name, "created": True}

# Endpoint PUT
@app.put("/items/{item_id}")
async def update_item(item_id: int, name: str):
    return {"item_id": item_id, "name": name, "update": True}

# Endpoint DELETE
@app.put("/items/{item_id}")
async def delete_item(item_id: int):
    return {"item_id": item_id, "deleted": True}

