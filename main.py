from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

app.mount("/scripts", StaticFiles(directory="scripts"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/')
def init(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request})

@app.get('/maths_questions')
def get_questions(request: Request):
    json_data = json.loads(open("questions.json").read())
    for item in json_data.values():
        print(item["Topic"])
        for no in item["question"]:
           print(item["question"][no])
    return templates.TemplateResponse("questions.html", {
        "request": request, "questions": json_data})

@app.post('save-answer')
async def save_answer(request: Request):
    data = await request.json()
    print(data)
    return {"status": "ok"}