from bittrex import Bittrex
import time
import pandas as pd


def get_values():
    sumary = bittrex.get_market_summaries()
    if sumary.get('success') != True:
        return -1
    else:
        return sumary.get('result')
    
bittrex = Bittrex(None, None)
    
while 1:
    res = get_values()
    if type(res) == int:
        continue
        
    df = pd.DataFrame(res)
    df.to_csv(str(time.time()))
    time.sleep(60)
