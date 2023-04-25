from flask import Flask, request
from db import stores, items
from flask_smorest import abort
import uuid


s = stores
b = items

app = Flask(__name__)

# print(stores)


@app.get("/store")
def get_stores():
    # return "Hello world"
    return {"Stores": list(stores.values())}, 200


@app.post("/store")
def post_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(
            400,
            message="Bad request, Ensure name is included in JSON payload",
        )
    for store in stores.values():
        if store_data["name"] == store["name"]:
            abort(400, message="Store already exists")

    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return stores, 201


@app.post("/item")
def add_item():
    item_data = request.get_json()
    if (
        "price" not in item_data
        or "name" not in item_data
        or "store_id" not in item_data
    ):
        abort(
            400,
            message="Bad request, Ensure price, store_id and name are included in JSON payload",
        )
    for item in items.values():
        if (
            item_data["name"] == item["name"]
            and item_data["store_id"] == item["store_id"]
        ):
            abort(400, message="Item already exists")
    if item_data["store_id"] not in stores:
        abort(404, message="Store not found")
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    return items


@app.get("/item")
def get_item():
    return {"items": list(items.values())}


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found")


@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"Message ": "Store Deleted"}
    except KeyError:
        abort(404, message="Store not found")


@app.get("/item/<string:item_id>")
def get_store_items(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found")


@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"Message ": "Item Deleted"}
    except KeyError:
        abort(404, message="Item not found")


@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_data = request.get_json()
    if "price" not in item_data or "name" not in item_data:
        abort(
            400,
            message="Bad request. Ensure 'price', and 'name' are included in the JSON payload.",
        )
    try:
        item = items[item_id]
        item |= item_data
        return item
    except KeyError:
        abort(404, message="Item not found")