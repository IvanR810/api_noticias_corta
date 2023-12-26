import urllib.request
import json

class Peticion:
    def __init__(self, q:str='all', language:str='es', page_size:int=20):
        self.url = f"https://newsapi.org/v2/everything?q={q}&language={language}&pageSize={page_size}&apiKey=cd8be6a615084a0d91c538e659a0790b"
        self.datos:dict = {}

    def __obtenerDatos(self):
        req = urllib.request.Request(self.url)

        with urllib.request.urlopen(req) as response:
            data = response.read().decode("utf-8")
            data = json.loads(data)

            self.datos = data
    
    def getDatos(self):
        self.__obtenerDatos()
        return self.datos