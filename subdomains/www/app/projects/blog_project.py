import requests
from app.projects.project import Project
from app.utils.markdown2html import markdown2html
from fastapi import APIRouter, Form, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


class Blog_Project(Project):
    def __init__(self, name, description, icon_path, route_base):
        super().__init__(name, description, icon_path, route_base)
        self.blogs = {
            "how_2_host": {
                "title": "how to have your own website",
                "description": "A Series of blogs about hosting a website",
                "blog_id": "how_2_host",
            },
            "how_2_static": {
                "title": "a bit about static sites",
                "description": "The static site part of the website blog",
                "blog_id": "how_2_static",
            },
            "how_2_cloud": {
                "title": "a bit about cloud hosting",
                "description": "The cloud part of the website blog",
                "blog_id": "how_2_cloud",
            },
            "how_2_home_server": {
                "title": "home server setup!",
                "description": "My favorite part of the website hosting article",
                "blog_id": "how_2_home_server",
            },
            "why_no_js": {
                "title": "why i avoid javascript",
                "description": "gaze upon me as I stand atop my soapbox and rant a bit about Javascript",
                "blog_id": "why_no_js",
            },
            # "": {"title": "", "description": "", "blog_id": ""},
        }

    def parse_template(self, request: Request):
        print(self.blogs.values())
        return self.templates.TemplateResponse(
            "projects/blog_project.html",
            {"request": request, "blogs": self.blogs.values()},
        )

    def parse_blog(self, request: Request, blog_id: str):
        blog = self.blogs.get(blog_id)
        with open(f"./static/assets/blogs/{blog_id}.md", "r") as f:
            content = f.read()
            content = markdown2html(request, content)
            return self.templates.TemplateResponse(
                "htmx_partials/blog.html",
                {
                    "request": request,
                    "title": self.blogs[blog_id]["title"],
                    "blog_content": content,
                },
            )


project = Blog_Project(
    "Blogs",
    "I be writing things",
    "assets/img/Cosmographie-Universelle-Guillaume-Le-Testu.png",
    "/blogs",
)
router = APIRouter()


@router.get("/blogs/")
async def blogs(request: Request):
    return project.parse_template(request)


@router.get("/blogs/{blog_id}")
async def get_blog(request: Request, blog_id: str):
    return project.parse_blog(request, blog_id)
