from enum import Enum
from typing import Optional

from fastapi import FastAPI

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, needy: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, "needy": needy}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/items/")
async def read_item_v2(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    _mapping = {
        ModelName.alexnet: "Deep Learning FTW!",
        ModelName.lenet: "LeCNN all the images",
        ModelName.resnet: "Have some residuals",
    }
    return {
        "model_name": model_name,
        "message": _mapping.get(model_name)
    }


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
