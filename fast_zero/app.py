from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Olá mundo!'}


@app.get('/html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def html():
    return '<h1>Olá mundo!</h1>'
