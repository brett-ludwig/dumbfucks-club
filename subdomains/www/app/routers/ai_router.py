from fastapi import APIRouter, Request, Response, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests
from collections import OrderedDict
from ollama import generate
from ollama import GenerateResponse



router = APIRouter()
templates = Jinja2Templates(directory="templates")
is_local = True

@router.post("/ai/send-message", response_class=HTMLResponse)
async def sendMessage(request: Request):
  if(is_local):
    form = await request.form()
    messageInput = form["messageInput"]
    systemPrompt = form["systemPrompt"]
    context = ""
    variables = { "messageInput":messageInput, "context":context}

    fullPrompt = systemPrompt.format(**variables)

    response: GenerateResponse = generate(model='mistral-nemo', prompt=messageInput, system=systemPrompt)
    response = response['response']
  else:
    response = "Currently this application only runs on my local machine (my server can't handle the LLM it doesn't have a GPU). If you pull the code for this website you can use this tool on your own local to interact with ollama chat models"
  # response = response.replace("\n", "<br>")
  # response = response.replace("\t", "<tab>")

  # or access fields directly from the response object
  return templates.TemplateResponse("ai_router/chatMessage.html", {"request": request, "response": response})


@router.get("/ai", response_class=HTMLResponse)
async def ai_view(request: Request):
    return templates.TemplateResponse("ai_router/ai.html", {"request": request} )
