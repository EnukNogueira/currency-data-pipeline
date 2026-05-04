from fastapi import FastAPI, Query
import requests
import json

app = FastAPI()

@app.get("/cotacao-dolar")
def obter_cotacao_dolar(pesquisa: float):
    url = "https://economia.awesomeapi.com.br/json/daily/USD-BRL/30"
    response = requests.get(url)
    data = response.json()

    for item in data:
        date = item.get('create_date', item.get('timestamp', 'desconhecida'))
        bid = item.get('bid')
        print(f"Valor encontrado: {bid} na data: {date}")

        try:
            if bid is not None and float(bid) == pesquisa:
                return {
                    "data_encontrada": date,
                    "valor_encontrado": f"O valor do dólar nessa data foi: {bid}"
                }
        except ValueError:
            continue
        
    return {"ERRO": "Valor não encontrado na cotação do dólar."}
        