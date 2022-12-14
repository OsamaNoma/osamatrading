from database import Signals
import numpy
import place_orders as po 
import requests
import telegram_msg as Tb 

def filter_order():
    data = []
    prev_data = [] # ["End_1", "BTCUSDT", "End_2", "ADAUSDT", "End_3", "End_4" , "End_5", "End_6"]
    all_lists = [ "End_1" , "End_2" , "End_3" , "End_4" , "End_5" , "End_6" ,"End_7", "End_8","End_9","End_10",
                   "End_11", "End_12", "End_13" ,"End_14" , "End_15" , "End_16" , "End_17" , "End_18" , "End_19" , "End_20" ,
                   "End_21" , "End_22" , "End_23" , "End_24" ,"End_25"] 

    x = 0
    all_tickers = {}
    while x < 25 : 
        x = 0
        data = Signals.find_all(collection = "Signals") # [{"End_1":0}, {"BTCUSDT":66548654}, {"End_2":0}, {"ADAUSDT":6546548}, {"End_3":0}, {"End_4":0}, {"End_5":0}, {"End_6":0}]
        tickers = list(data.keys()) # ["End_1", "BTCUSDT", "End_2", "ADAUSDT", "End_3", "End_4" , "End_5", "End_6"]
        if tickers != prev_data:
            for ticker in tickers:
                if ticker not in prev_data and "USDT" in ticker:
                    all_tickers[ticker] = data[ticker] #{"BTCUSDT":66548654, "ADAUSDT":6546548}
                if ticker in all_lists:
                    x = x+1 #1, 2, 3, 4, 5, 6
        prev_data = tickers 

    sorted_tickers = sorted(all_tickers.items(), key = lambda x: x[1], reverse = True)
    if sorted_tickers:
        selected_ticker = sorted_tickers[0][0] #"BTCUSDT"
        pct_change = (sorted_tickers[0][1][1] * -1) # 3.5
        if selected_ticker != None and pct_change != None:
            balance = po.get_usdt_balance()
            if balance >= 20:
                print("Entry amount :", balance, "USDT")
                print("Symbol:", selected_ticker)
                tkr, avgPrice, id = po.buy_market(symbol = selected_ticker, amount = balance)
                print("Buy order placed successfully")
                print("Entry price :", str(avgPrice))
                detail, tp, trigger, sl = po.oco_order_sell(symbol = tkr, avg_price = avgPrice, pct_sl = pct_change)
                print("OCO order placed successfully")
                print("Take profit:", str(tp))
                print("Stop price :", trigger)
                print("Stoplimit :", sl)
                avg_price = round(float(avgPrice), 5)
                print("Place order for :", selected_ticker, "Entry price :", str(avg_price))
            else :
                print("Insuffiant balance!"),Tb.send_message("Insuffiant balance!")
    else:
        print("No order placed!"),Tb.send_message("No order placed!") 
    print("---------------------------------------------------")
    
    Signals.clear_all(collection = "Signals")