from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Secure and Scalable App"}

@app.get("/items")
def read_items():
    return {"message": "GET request received"}

@app.post("/items")
def create_item():
    return {"message": "POST request received"}

@app.put("/items/{item_id}")
def update_item(item_id: int):
    return {"message": f"PUT request received for item {item_id}"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"DELETE request received for item {item_id}"}
