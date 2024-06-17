from fastapi import FastAPI, Request, Response, Form, File, Depends, HTTPException, status
from fastapi.responses import  RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')

@app.get("/")
async def index(request:Request):
    return templates.TemplateResponse('index.html', {"request":request})

if __name__ == '__main__':
    uvicorn.run("app:app", host='0.0.0.0',port=8080, reload=True)