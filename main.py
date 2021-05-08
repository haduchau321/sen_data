from fastapi import FastAPI
import uvicorn
import author

key = 'haduchau_admin'
app = FastAPI()

@app.get('/send/{ip}/{vitri}/{data}')
async def send(ip:str,vitri:str,data:str):
    print(ip,vitri,data)
    author.send(ip,vitri,data)
    return True

@app.get('/api_key={api_key}')
async def send(api_key:str):
    if api_key == key:
        out = author.get_data()
        return out

uvicorn.run(app)

#  {"id_sy":"AQE5yR7GMR_37vQ:AQFZ_gcVHE0wO-M","id_post":"22412"}