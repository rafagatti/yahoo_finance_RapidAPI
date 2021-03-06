import requests as rq
import json
from decorador import gerador_try_except


class YahooFinance():
    
    def __init__(self, secret, ativo, region, host = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock'):
        
        self.headers = {
            'x-rapidapi-key': str(secret),
            'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
            }
        self.secret = secret
        self.ativo = ativo
        self.region = region
        self.host = host

    @gerador_try_except
    def historico_ativo(self, endpoint = 'v3/get-historical-data'):
        
        url = '{}/{}'.format(self.host, endpoint)

        querystring = {"symbol":str(self.ativo),"region":str(self.region)}
        response = rq.get(url, headers=self.headers, params=querystring)
        
        return json.loads(response.text)



if __name__ == '__main__':

    ativo_amrn = YahooFinance(secret = '', region = 'US' , ativo = 'AMRN')
    historico_amrn = ativo_amrn.historico_ativo()

    print(historico_amrn)