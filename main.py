from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/irishpubs/api/all")
async def get_pubs():
    return {"message": "Hello"}


@app.get("/irishpubs/api/{name}")
async def get_pub(name: str):
    return {"message": f"Hello {name}"}


@app.get("/irishpubs/api/{county}")
async def get_pub(name: str):
    return {"message": f"Hello {name}"}

@app.delete("/irishpubs/api/{id}")
async def get_pub(name: str):
    return {"message": f"Hello {name}"}