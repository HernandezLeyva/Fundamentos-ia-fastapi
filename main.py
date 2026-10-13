from searching import bfs_search,dfs_search,hill_climbing_search
from fastapi import FastAPI

app = FastAPI()

#TAREAS CONTRA METODOS 
#Create post 
#Read- get 
#Update- put 
#Delete- Delete

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.post("/bfs")
def bfs_search(item_id:dict):
    resultado = bfs_search()
    return {"item_id: Aqui se implementa la busqueda bfs"}

@app.post("/dfs")
def dfs_search(item_id:dict):
    resultado = dfs_search()
    return {"item_id: Aqui se implementa la busqueda dfs"}

@app.post("/hill-climbing")
def hill_climbing_search(item_id:dict):
    resultado = hill_climbing_search()
    return {"item_id: Aqui se implementa la busqueda de escalada"}