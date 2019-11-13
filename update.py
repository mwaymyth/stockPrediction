import requests
import json
import csv

api_key = "AIGDL0I4XDSHIND8"
URL = "https://www.alphavantage.co/query"


def update(symbol, in_csv):
    file_out = "./" + in_csv
    PARAMS = {
            'function': "TIME_SERIES_DAILY",
            'symbol': symbol,
            'datatype': "csv",
            'outputsize':"full",
            'apikey': api_key
            }
    response = requests.get(url=URL, params=PARAMS)
    f = open(file_out,'w')
    f.write(response.text)
    f.close()
    

