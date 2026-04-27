import requests
from app.projects.project import Project
from fastapi import APIRouter, Form, Request, Response
from fastapi.responses import HTMLResponse


# HTMX powered logic to update a chat frontend
class Squash_The_Creeps_Project(Project):
    def parse_template(self, request: Request):
        return self.templates.TemplateResponse(
            "projects/squash-the-creeps.html", {"request": request}
        )


project = Squash_The_Creeps_Project(
    "Demo HTML Game",
    "Very out of date. Just wanted to try hosting an HTML5 game",
    "assets/img/squash-the-creeps.png",
    "/squash-the-creeps",
)
router = APIRouter()


@router.get("/squash-the-creeps", response_class=HTMLResponse)
async def squash_the_creeps(request: Request):
    return project.parse_template(request)
