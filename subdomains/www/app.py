from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from collections import OrderedDict

from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
import requests



origins = [
    "http://www.dumbfucks.club"
]
CSP: dict[str, str | list[str]] = {
    "default-src": "'self'",
    "img-src": [
        "https://www.dumbfucks.club"
    ],
    "script-src": [
        "'wasm-unsafe-eval'",
        "https://www.dumbfucks.club"
    ],
    "style-src": [
        "https://www.dumbfucks.club"
    ],
    "script-src-elem": [
        "https://www.dumbfucks.club"
    ],
    "script-src-elem": [
        "https://www.dumbfucks.club"
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
app.add_middleware(SecurityHeadersMiddleware, csp=True)

stats = ["attack", "defence", "strength", "hitpoints", "ranged", "prayer", "magic", "cooking", "woodcutting", "fletching", "fishing", "firemaking", "crafting", "smithing", "mining", "herblore", "agility", "thieving", "slayer", "farming", "runecrafting", "hunter", "construction"]


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request} )
    
@app.get("/squash-the-creeps", response_class=HTMLResponse)
async def squash_the_creeps(request: Request):
    return templates.TemplateResponse("portfolio/squash-the-creeps.html", {"request": request} )
    
@app.get("/this-website", response_class=HTMLResponse)
async def squash_the_creeps(request: Request):
    return templates.TemplateResponse("portfolio/this-website.html", {"request": request} )

@app.get("/dnd", response_class=HTMLResponse)
async def dnd(request: Request):
    return templates.TemplateResponse("portfolio/dnd.html", {"request": request} )

def getCurrentOsrsStats(playerName:str):
    response = requests.get(f"https://api.wiseoldman.net/v2/players/{playerName}")
    playerData = response.json()
    playerStats = {}
    for stat in stats:
        playerStats[stat] =  playerData["latestSnapshot"]["data"]["skills"][stat] #[stat]["level"]
    
    return playerStats

def updatePlayer(playerName:str):
    response = requests.post(f"https://api.wiseoldman.net/v2/players/{playerName}")
    print(response)
    print(response.text)

@app.get("/runescape", response_class=HTMLResponse)
async def runescape(request: Request):
    SchnozmoBTW = getCurrentOsrsStats("SchnozmoBTW")
    ChetJubetcha = getCurrentOsrsStats("ChetJubetcha")
    PamelaWett = getCurrentOsrsStats("Pamela Wett")
    TrixieTng = getCurrentOsrsStats("TrixieTng")

    return templates.TemplateResponse("portfolio/runescape.html", {"request": request, "SchnozmoBTW": SchnozmoBTW, "ChetJubetcha":ChetJubetcha, "PamelaWett":PamelaWett, "TrixieTng":TrixieTng, "stats": stats})