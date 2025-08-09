from fastapi import FastAPI

app = FastAPI()

# Implement the Hello World endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello World"}

