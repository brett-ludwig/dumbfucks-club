from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from collections import OrderedDict

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
import requests
from app.projects import ai_project, blog_project, squash_the_creeps_project, dnd_project



origins = [
    "http://www.dumbfucks.club",
    "http://redyard:50002",
]
CSP: dict[str, str | list[str]] = {
    "default-src": "'self'",
    "img-src": [
        "https://www.dumbfucks.club",
        "http://redyard:50002",
    ],
    "script-src": [
        "'wasm-unsafe-eval'",
        "https://cdn.jsdelivr.net/npm/htmx.org@2.0.6/dist/htmx.min.js",
        "sha384-Akqfrbj/HpNVo8k11SXBb6TlBWmXXlYQrCSqEWmyKJe+hDm3Z/B2WVG4smwBkRVm",
        "https://www.dumbfucks.club",
        "http://redyard:50002",
    ],
    "style-src": [
        "https://www.dumbfucks.club",
        "http://redyard:50002",
    ],
    "script-src-elem": [
        "https://www.dumbfucks.club",
        "https://cdn.jsdelivr.net/npm/htmx.org@2.0.6/dist/htmx.min.js",
        "sha384-Akqfrbj/HpNVo8k11SXBb6TlBWmXXlYQrCSqEWmyKJe+hDm3Z/B2WVG4smwBkRVm",
        "http://redyard:50002",
    ],
}

local = True
if local:
    origins.append("localhost")
    for k in CSP:
        if k != "default-src":
            CSP[k].append("localhost:8000")



class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Add security headers to all responses."""

    def __init__(self, app: FastAPI, csp: bool = True) -> None:
        """Init SecurityHeadersMiddleware.

        :param app: FastAPI instance
        :param no_csp: If no CSP should be used;
            defaults to :py:obj:`False`
        """
        super().__init__(app)
        self.csp = csp
        
    def parse_policy(self, policy: dict[str, str | list[str]] | str) -> str:
        """Parse a given policy dict to string."""
        if isinstance(policy, str):
            # parse the string into a policy dict
            policy_string = policy
            policy = OrderedDict()
    
            for policy_part in policy_string.split(";"):
                policy_parts = policy_part.strip().split(" ")
                policy[policy_parts[0]] = " ".join(policy_parts[1:])
    
        policies = []
        for section, content in policy.items():
            if not isinstance(content, str):
                content = " ".join(content)
            policy_part = f"{section} {content}"
    
            policies.append(policy_part)
    
        parsed_policy = "; ".join(policies)
    
        return parsed_policy

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        """Dispatch of the middleware.

        :param request: Incoming request
        :param call_next: Function to process the request
        :return: Return response coming from from processed request
        """
        headers = {
            "Content-Security-Policy": "" if not self.csp else self.parse_policy(CSP),
            "Cross-Origin-Opener-Policy": "same-origin",
            "Cross-Origin-Embedder-Policy": "require-corp",
            "Referrer-Policy": "strict-origin-when-cross-origin",
            "Strict-Transport-Security": "max-age=31556926; includeSubDomains",
            "X-Content-Type-Options": "nosniff",
            "X-Frame-Options": "DENY",
            "X-XSS-Protection": "1; mode=block",
        }
        response = await call_next(request)
        response.headers.update(headers)

        return response


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

projects = [ blog_project.project, ai_project.project, squash_the_creeps_project.project, dnd_project.project]
routers = [blog_project.router, ai_project.router, squash_the_creeps_project.router,  dnd_project.router]

for router in routers:
    app.include_router(router)

app.add_middleware(SecurityHeadersMiddleware, csp=True)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request): 
    return templates.TemplateResponse("index.html", {"request": request, "projects": projects} )

@app.get("/cypress", response_class=HTMLResponse)
async def cypress(request: Request, keyframe):
    keyframe = int(keyframe) + 1
    if(keyframe == 7):
        keyframe = 1

    img_path = "assets/img/Cypress_anim%d.png" % keyframe
    print(img_path)
    return templates.TemplateResponse("htmx_partials/cypress_animation.html", {"request": request, "img_path":img_path, "keyframe":keyframe} )

    



