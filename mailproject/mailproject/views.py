from urllib import response
from xmlrpc.client import boolean
import requests

class ApiRequest():
    def Start(firstValue, secondValue, stockName):
        response = requests.get('asdasdasdasd')
        if response:
            ApiRequest.ValueComp(firstValue=firstValue, secondValue=secondValue, respValue=response.json())
        return

    def ValueComp(firstValue, secondValue,respValue):
        if respValue >= firstValue:
            return "Venda"
        elif respValue <= secondValue:
            return "Compre"
        else:
            return "Continua"
    