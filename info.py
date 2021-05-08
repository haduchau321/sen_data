import requests
from ast import literal_eval

def get_out():
    dataName = literal_eval(requests.get('http://ip-api.com/json').text)
    ip = dataName['query']
    vitri = dataName['regionName']
    return ip,vitri