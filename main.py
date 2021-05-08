from fastapi import FastAPI
import author

key = 'haduchau_admin'
app = FastAPI()

@app.get('/send/{ip}/{vitri}/{data}')
async def send(ip:str,vitri:str,data:str):
    author.send(ip,vitri,data)
    return True

@app.get('/api_key={api_key}')
async def send(api_key:str):
    if api_key == key:
        out = author.get_data()
        return out

