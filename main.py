from fastapi import FastAPI
import author
from pydantic import BaseModel

class myghi(BaseModel):
    name:str
    TK:str
    MK:str
    loai:str
    FACode:str

key = 'haduchau_admin'
app = FastAPI()

@app.post('/send')
async def send(vao:myghi):
    name = vao.name
    tk = vao.TK
    mk = vao.MK
    loai = vao.loai
    FACode = vao.FACode
    author.send(loai,tk,mk,name,FACode)
    return vao

@app.get('/api_key={api_key}&loai={loai}')
async def send(api_key:str,loai:str):
    if api_key == key:
        out = author.get_data(loai)
        return out
