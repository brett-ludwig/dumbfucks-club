from fastapi import APIRouter, Request, Response, Form
from fastapi.responses import HTMLResponse
import requests
from app.projects.project import Project


# HTMX powered logic to update a chat frontend
class DnD_Project(Project):


  def parse_template(self, request: Request):
    return self.templates.TemplateResponse("projects/dnd.html", {"request": request} )


project = DnD_Project("DnD", "DnD Landing Page", "assets/img/dnd-logo.jpg", "/dnd")
router = APIRouter()

@router.get("/dnd", response_class=HTMLResponse)
async def dnd(request: Request):
    return project.parse_template(request)