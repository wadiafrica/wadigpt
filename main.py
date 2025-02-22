from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from chainlit.utils import mount_chainlit


app = FastAPI()

origins = ['https://app.wadi.africa', 'http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response: Response = await call_next(request)

        response.headers['X-Frame-Options'] = 'ALLOWALL'

        response.headers[
            'Content-Security-Policy'
        ] = "frame-ancestors 'self' https://app.wadi.africa;"

        return response


app.add_middleware(SecurityHeadersMiddleware)


@app.get('/')
async def root():
    return {'message': "Wadi's FastAPI is running! ⚡️"}


# Mount Chainlit apps
mount_chainlit(app=app, target='wadigpt.py', path='/wadigpt')
mount_chainlit(app=app, target='chat.py', path='/chat')
