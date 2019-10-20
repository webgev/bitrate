
import urllib
import json
from datetime import datetime, timedelta

URL = 'https://api-pub.bitfinex.com/v2/candles/trade:1D:t{currency}USD/hist?start={start}&end={end}'

def get_rate(currency):
    """
    Вернет информацию по валюте по api bitfinex
    """
    
    result = []
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'access-control-allow-origin': '*',
        'User-Agent': 'Mozilla/5.0',
    }
    # timestamp приходит с суффиксом "000", поэтому его нужно обрезать
    time_suffix = "000" 
    end = str(int(datetime.now().timestamp())) + time_suffix
    start = str(int((datetime.now() - timedelta(days=10)).timestamp())) + time_suffix
    url = URL.format(currency=currency, start=start, end=end)

    req = urllib.request.Request(url.format(currency=currency), None, headers)
    try:
        with urllib.request.urlopen(req) as response:
            res = response.read()
            if res:
                res = json.loads(res)
                for rec in res:
                    date = str(rec[0])[:-len(time_suffix)]
                    date = datetime.fromtimestamp(int(date)).date()
                    result.append({"rate": rec[2], "volume": rec[5], "date":date})
    except Exception as ex:
        print("Ошибка при обработке api bitfinex " + str(ex)) 
    return result