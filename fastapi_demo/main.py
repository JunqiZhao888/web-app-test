from fastapi import FastAPI echo app = FastAPI() echo @app.get('/') echo async def read_root(): echo     return {"message": "Hello, World!"}
