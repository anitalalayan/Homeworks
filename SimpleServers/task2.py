from fastapi import FastAPI, HTTPException


app = FastAPI()

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]
products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Smartphone", "price": 500}
]


@app.get("/users")
async def get_users()-> list[dict]:
    return users

@app.get("/products")
async def get_products()-> list[dict]:
    return products

@app.get("/users/{user_id}")
async def get_user(user_id: int)-> dict:
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/products/{product_id}")
async def get_product(product_id: int)-> dict:
    product = next((product for product in products if product["id"] == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/users")
async def create_user(user: dict) -> dict:
    for u in users:
        if u["id"] == user["id"]:
            raise HTTPException(status_code=409, detail="User already exists")

    users.append(user)
    return {"message": "User added to the database", "user": user}

@app.post("/products")
async def create_product(product: dict) -> dict:
    for product in products:
        if product["id"] == product["id"]:
            raise HTTPException(status_code=409, detail="Product already exists")

    products.append(product)
    return {"message": "Product added to the database", "product": product}

@app.put("/users/{id}")
async def update_user(id: int, data: dict)-> dict:
    for user in users:
        if user["id"] == id:
            for key, value in data.items():
                if key in user:
                    user[key] = value
            return {"message": "User updated successfully", "user": user}

    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{id}")
async def delete_user(id: int)-> dict:
    for user in users:
        if user["id"] == id:
            users.pop(users.index(user))
            return {"message": "User deleted successfully", "user": user}
