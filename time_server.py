from binance_client import client
import requests
from datetime import datetime
import time as t 
import requests
import pandas as pd
import threading
import tickers as tkr
import engulfing_2_ema_stgy as stgy
import filter_orders as fo
import telegram_msg as Tb

interval = [0, 15, 30, 45]

def server_tm():
    time_srv = client.get_server_time()
    time = pd.to_datetime(time_srv["serverTime"], unit = "ms")
    min_ = (time.strftime("%M"))
    min_ = int(min_)
    sec_ = time.strftime("%S")
    sec_ = int(sec_)
    for i in interval:
        if min_ == i and sec_ == 3:
            print("Searching for opportunities ..."),Tb.send_message("Searching for order ..")
            # run strategy
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_1, 1)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_2, 2)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_3, 3)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_4, 4)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_5, 5)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_6, 6)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_7, 7)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_8, 8)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_9, 9)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_10, 10)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_11, 11)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_12, 12)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_13, 13)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_14, 14)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_15, 15)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_16, 16)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_17, 17)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_18, 18)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_19, 19)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_20, 20)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_21, 21)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_22, 22)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_23, 23)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_24, 24)).start()
            threading.Thread(target = stgy.engulfing_strgy, args = (tkr.list_25, 25)).start()
            threading.Thread(target = fo.filter_order).start()
            t.sleep(5)

        
            

            