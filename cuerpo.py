from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

class User(BaseModel):
    username: str
    full_name: str = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.post("/item/{item_id}")
async def create_item(item_id: int, item: Item, user: User):
    return {"item_id": item_id, "item": item, "user": user}