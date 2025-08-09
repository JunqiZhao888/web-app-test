from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Implement the Hello World endpoint
@app.get("/")
async def read_root():
    return templates.TemplateResponse("index.html", {"request": {}})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")



