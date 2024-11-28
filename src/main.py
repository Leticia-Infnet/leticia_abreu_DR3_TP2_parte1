from fastapi import FastAPI
from routers.chat import router as AutocompleteRouter
from routers.translator import router as TranslatorRouter

app = FastAPI()

app.include_router(router=AutocompleteRouter,
                   prefix='/chat',
                   tags=['chat'])

app.include_router(router=TranslatorRouter,
                   prefix='/translate',
                   tags=['translate'])


@app.get('/status')
async def status():
    return {'message': 'O server está rodando!'}
