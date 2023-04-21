from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "Store1",
        "items": [
            {"item": "chair", "price": 100},
            {"item": "Book", "price": 50},
        ],
    },
    {
        "name": "Store2",
        "items": [
            {"item": "table", "price": 200},
            {"item": "Pen", "price": 20},
        ],
    },
]

# print(stores)


@app.get("/store")
def get_stores():
    return {"Stores": stores}, 200


@app.post("/store")
def post_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return stores, 201


@app.post("/store/<string:name>/item")
def add_item(name):
    request_body = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"item": request_body["item"], "price": request_body["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return "Message: Store not found", 404


@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store, 201
    return "Message: Store not found", 404


@app.get("/store/<string:name>/items")
def get_store_items(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}, 201
    return "Message: Store not found", 404
