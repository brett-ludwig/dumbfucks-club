from fastapi import APIRouter, Request, Response, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests



router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/squash-the-creeps", response_class=HTMLResponse)
async def squash_the_creeps(request: Request):
    return templates.TemplateResponse("portfolio/squash-the-creeps.html", {"request": request} )