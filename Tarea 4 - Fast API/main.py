import io
from enum import Enum
from typing import Optional

import pandas as pd
from fastapi import FastAPI, Response
from pydantic import BaseModel
import random

from fastapi.responses import ORJSONResponse, UJSONResponse, HTMLResponse, PlainTextResponse, RedirectResponse, StreamingResponse, FileResponse

app = FastAPI()

class RoleName(str, Enum):
    admin = 'admin'
    writer = 'writer'
    reader = 'reader'

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None



fake_items_db = [{'item_name': 'uno'}, {'item_name': 'dos'}, {'item_name': 'tres'}]

@app.get('/')
def root():
    return {'message': 'Hello World, From Galileo Master!'}


@app.get('/items/all', response_class=ORJSONResponse)
def read_all_items():
    return [{'item_id': 'un item'}, {'item_id': 'un item'}, {'item_id': 'un item'}, {'item_id': 'un item'},
            {'item_id': 'un item'}, {'item_id': 'un item'}, {'item_id': 'un item'}, {'item_id': 'un item'}]


@app.get('/items/all/alternative', response_class=UJSONResponse)
def read_all_items_alternative():
    return [{'item_id': 'un item'}, {'item_id': 'un item'}, {'item_id': 'un item'}, {'item_id': 'un item'},
            {'item_id': 'un item'}, {'item_id': 'un item'}, {'item_id': 'un item'}, {'item_id': 'un item'}]




# Las rutas deben ser únicas
@app.get('/items/{item_id}')
def read_item(item_id: int, query: Optional[str] = None):
    if query:
        return {'item_id': item_id, 'query': query}
    return {'item_id': item_id}

# Solicita un usuario
@app.get('/users/current')
def read_current_user():
    return {'user_id': 'The current user'}

# Envía un usuario
@app.get('/users/{user_id}')
def read_user(user_id: str):
    return {'user_id': user_id}

#El orden de las funciones importa


@app.get('/roles/{rolename}')
def get_role_permissions(rolename: RoleName):
    if rolename == RoleName.reader:
        return {'role': rolename, 'permissions': 'you are allowed only to read'}

    if rolename == 'writer':
        return {'role': rolename, 'permissions': 'you are allowed read and write'}

    return {'role': rolename, 'permissions': 'you have all access'}



@app.get('/items')
def read_all_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]



@app.get('/users/{user_id}/item/{item_id}')
def read_user_items(user_id: int, item_id: int, query: Optional[str] = None, short: bool = False):
    item = {'item_id': item_id, 'owner': user_id}

    if query:
        item-update({'query': query})

    if not short:
        item.update({'description': 'This is a long description for the item selected'})

    return item


@app.post('/items/')
def create_item(item: Item):
    if not item.tax:
        item.tax = item.price * 0.12

    return {'item_id': random.randint(1, 100), **item.dict()}


@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'msg': f'El item {item_id} fue actualizado', 'item': item.dict()}



@app.get('/html', response_class=HTMLResponse)
def get_html():
    return '''
    <html>
        <head>
            <title> Some title here </title>
        </head>
        <body>
            <h1> Look is HTML! </h1>
        </body>
    </html>
    '''



@app.get('/legacy')
def get_legacy_response():
    data = '''
    <?xml version='1.00?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    '''

    return Response(content=data, media_type='application/xml')


@app.get('/plain', response_class=PlainTextResponse)
def get_plain_text():
    return 'Hello World'



@app.get('/redirect')
def redirect():
    return RedirectResponse('https://google.com')

@app.get('/video')
def show_video():
    video_file = open('ejemplo.mp4', mode='rb')
    return StreamingResponse(video_file, media_type='video/mp4')


@app.get('/video/download')
def download_video():
    return FileResponse('ejemplo.mp4')


@app.get('/csv')
def download_csv():
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

    stream = io.StringIO()

    df.to_csv(stream, index=False)

    response = StreamingResponse(iter([stream.getvalue()]), media_type='text/csv')

    response.headers['Content-Disposition'] = 'attachment; filename=export.csv'

    return response
