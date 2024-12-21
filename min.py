from fastapi import FastAPI
app = FastAPI()


items=[]
@app.post("/items")
def cretaeitem(item : str):
    items.append(item)
    return items

@app.delete("/items/{item_name}")
def delete_item(item_name: str):
    if item_name in items:
        items.remove(item_name)
        return {"message": f"Item '{item_name}' deleted", "items": items}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app,host="127.0.0.1", port=8000)
    