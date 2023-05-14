from fastapi import FastAPI
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup

app = FastAPI()


class Url(BaseModel):
    url: str


class Element(BaseModel):
    url: str
    property: str


def parse_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


# check if server is running
@app.get("/")
async def root():
    return {"status": "200", "message": "hello from fastapi"}


# get html page
@app.post("/")
async def root(url: Url):
    soup = parse_url(url.url)
    return {"page": str(soup)}


# get title of html page
@app.post("/title")
async def root(url: Url):
    soup = parse_url(url.url)
    return {"title": soup.title.string}


# get particular element of html page
@app.post("/element")
async def root(url: Element):
    soup = parse_url(url.url)
    elements = []
    for element in soup.find_all(url.property):
        elements.append(str(element))
    return {"elements": elements}


# get all links of html page
@app.post("/links")
async def root(url: Url):
    soup = parse_url(url.url)
    links = []
    for link in soup.find_all("a"):
        links.append(link.get("href"))
    return {"links": links}


# get the elements of html page with particular class
@app.post("/class")
async def root(url: Element):
    soup = parse_url(url.url)
    elements = []
    for element in soup.find_all(class_=url.property):
        elements.append(str(element))
    return {"class": elements}


# get the elements of html page with particular id
@app.post("/id")
async def root(url: Element):
    soup = parse_url(url.url)
    elements = []
    for element in soup.find_all(id=url.property):
        elements.append(str(element))
    return {"id": elements}
