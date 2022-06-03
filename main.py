from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"name":"Veysel"}

@app.get("/x")
async def index():
    return {"name":"hamdi"}
