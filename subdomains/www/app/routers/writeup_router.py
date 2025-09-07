from fastapi import APIRouter, Request, Response, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests



router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/this-website", response_class=HTMLResponse)
async def this_website(request: Request):
    return templates.TemplateResponse("portfolio/this-website.html", {"request": request} )

@router.get("/css-opinions", response_class=HTMLResponse)
async def this_website(request: Request):
    return templates.TemplateResponse("portfolio/css-opinions.html", {"request": request} )
