from all_route import router as signup
from login import router as login
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Create FastAPI app
app = FastAPI()
app.include_router(signup)
app.include_router(login)
# Setup templates folder
templates = Jinja2Templates(directory="templates")

# Route to render the HTML page
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
