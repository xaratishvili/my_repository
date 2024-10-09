from fastapi import FastAPI, HTTPException

from crud import create_item, get_items, get_item_by_id
from dependencies import get_database
from schemas import ItemRead, ItemCreate
from tortoise import Tortoise
from tortoise.models import Model
from tortoise import fields

app = FastAPI()

Tortoise.init(
    db_url='postgres://postgres:123@localhost:5432/new',
    modules={'models': ['app.models']}
)


class Item(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    description = fields.TextField()


# Update record
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    existing_item = await Item.filter(id=item_id).first()
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item not found")

    existing_item.name = item.name
    existing_item.description = item.description
    await existing_item.save()
    return existing_item

@app.post("/items/", response_model=ItemRead)
async def create_new_item(item: ItemCreate):
    return await create_item(item)


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    existing_item = await Item.filter(id=item_id).first()
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item not found")

    await existing_item.delete()
    return {"message": "Item deleted successfully"}


@app.get("/", response_model=list[ItemRead])
async def read_all_items():
    return await get_items()


@app.get("/{item_id}", response_model=ItemRead)
async def read_one_item(item_id: int):
    item = await get_item_by_id(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item



get_database(app)