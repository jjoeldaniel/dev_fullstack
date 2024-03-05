from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import json


class Event:
    def __init__(self, data: dict[str, str]) -> None:
        self.name = data["name"]
        self.location = data["location"]
        self.date = data["date"]
        self.description = data["description"]


with open("events.json") as f:
    json_data = json.load(f)

data: list[Event] = []

for event in json_data["events"]:
    data.append(Event(event))


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


@app.get("/hello", response_class=HTMLResponse)
async def hello(request: Request, name: str = "stranger"):
    return templates.TemplateResponse(
        request=request, name="hello.html", context={"name": name}
    )


@app.get("/events", response_class=HTMLResponse)
async def events(request: Request):
    return templates.TemplateResponse(
        request=request, name="events.html", context={"data": data}
    )


@app.get("/api/name")
async def getName():
    return {"name": "Joel"}
