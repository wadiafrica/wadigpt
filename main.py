from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chainlit.utils import mount_chainlit


app = FastAPI()


origins = ['https://app.wadi.africa/', 'http://localhost:3000']


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get('/')
async def root():
    return {'message': "Wadi's FastAPI is running! ⚡️"}


mount_chainlit(app=app, target='wadigpt.py', path='/wadigpt')
# mount_chainlit(app=app, target='chat.py', path='/chat')
