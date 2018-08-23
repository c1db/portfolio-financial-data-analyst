import requests
import urllib
import csv
import time
import datetime

def find_large_orders(seq, t):
    # seq - последовательность ордеров в стакане, t - тип ордера(на покупку или продажу)
    for i in seq:
        # обходим ордера, ищем соотвествующие условию
        amount_cont = i[1]
        amount = amount_cont*100/index
        if amount >= 450:   # условие - ордер превышает 450 бтц 
            
            ti = time.time()    # записываем время
            ti = int(ti)
            q = datetime.datetime.fromtimestamp(ti)
            
            # определяем тип ордера для оповещения, пишем в консоль оповещение "тип ордера\размер\время"
            
            if t == 1:         
                print ('bid alert', i, q)
            if t == 2:
                print ('ask alert', i, q)
            return 0
    return -1
    
depth_url = 'https://www.okex.com/api/v1/future_depth.do?symbol=btc_usd&contract_type=quarter&size=20'
index_url = 'https://www.okex.com/api/v1/future_index.do?symbol=btc_usd'
history_url = 'https://www.okex.com/api/v1/future_trades.do?symbol=btc_usd&contract_type=quarter'
iterable = 0    # переменная для записи последних сделок при обнаружении больших ордеров в стакане
file = open('hist.csv', 'a')

while(1):
    
    try:
        
        if iterable > 0: # если есть большой ордер - записываем последние сделки, уменьшаем счетчик на 1

            req_hist = requests.get(history_url)
            hist = req_hist.json()
            csv_file = csv.writer(file)
            for i in hist:
                csv_file.writerow([i['date_ms'], i['amount'], i['tid'], i['price'], i['date'], i['type']])
            iterable = iterable - 1

        req_indx = requests.get(index_url) # получаем значение индекса в данный момент
        index = req_indx.json()['future_index']
        depth_req = requests.get(depth_url) # получаем состояние стакана

        # обработка ошибок на случай проблем подключения
        try:   
            depth = depth_req.json()
        except:
            print ("error")

        bids = depth['bids']
        asks = depth['asks']

        if (find_large_orders(bids, 1) == 0) or (find_large_orders(asks, 2) == 0): # если в стакане есть большие ордера - 
                                                                                   # включаем запись на следующую 21 итерацию
            iterable = 21
        time.sleep(5)
    except:
        pass