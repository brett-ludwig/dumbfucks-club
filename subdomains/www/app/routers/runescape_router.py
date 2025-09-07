from fastapi import APIRouter, Request, Response, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests
from datetime import datetime, timedelta




router = APIRouter()
templates = Jinja2Templates(directory="templates")
# use so by default first request updates empty cache
old_datetime = datetime.fromisoformat('2011-11-04')
cache_timers = {"SchnozmoBTW": old_datetime, "ChetJubetcha": old_datetime, "Pamela Wett": old_datetime, "TrixieTng": old_datetime}
cache_delta = timedelta(minutes=30)

players = {"SchnozmoBTW": {}, "ChetJubetcha": {}, "Pamela Wett": {}, "TrixieTng": {}}

stats = ["attack", "defence", "strength", "hitpoints", "ranged", "prayer", "magic", "cooking", "woodcutting", "fletching", "fishing", "firemaking", "crafting", "smithing", "mining", "herblore", "agility", "thieving", "slayer", "farming", "runecrafting", "hunter", "construction"]

@router.get("/getStats")
async def getCurrentOsrsStats(request: Request, playerName: str):
    dt_now = datetime.now()
    if (dt_now - cache_timers[playerName] > cache_delta):
        print(playerName)
        response = requests.get(f"https://api.wiseoldman.net/v2/players/{playerName}")
        playerData = response.json()
        if("message" in playerData):
            return templates.TemplateResponse("runescape_router/statblock.html", {"request": request, "stats": stats, "playerName": playerName, "statDetails": players[playerName]})
        playerStats = {}
        for stat in stats:
            playerStats[stat] =  playerData["latestSnapshot"]["data"]["skills"][stat] #[stat]["level"]
        players[playerName] = playerStats
        cache_timers[playerName] = dt_now
    return templates.TemplateResponse("runescape_router/statblock.html", {"request": request, "stats": stats, "playerName": playerName, "statDetails": players[playerName]})

async def updatePlayer(playerName:str):
    response = requests.post(f"https://api.wiseoldman.net/v2/players/{playerName}")


@router.get("/runescape", response_class=HTMLResponse)
async def runescape(request: Request):
    return templates.TemplateResponse("runescape_router/runescape.html", {"request": request, "SchnozmoBTW": players["SchnozmoBTW"], "ChetJubetcha": players["ChetJubetcha"], "PamelaWett":players["Pamela Wett"], "TrixieTng":players["TrixieTng"], "stats": stats})