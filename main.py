from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


# @app.get("/hello", response_class=HTMLResponse)
# async def hello1(request: Request):
#     return templates.TemplateResponse(request=request, name="hello.html")


@app.get("/hello/", response_class=HTMLResponse)
async def hello(request: Request, name: str = "stranger"):
    return templates.TemplateResponse(
        request=request, name="hello.html", context={"name": name}
    )


@app.get("/api/name")
async def getName():
    return {"name": "Joel"}
