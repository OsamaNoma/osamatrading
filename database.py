import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["KitoTrading_bot"]

class Status(): 
    def save_status(collection, status, time):
        collection = db[collection]
        data = collection.delete_one({})
        new_stat = {"Status":status, "Time":time}
        data = collection.insert_one(new_stat)
        return data

    def find_status(collection):
        collection = db[collection]
        data = collection.find({})
        for dt in data:
            stat = dt["Status"]
        return stat 

class Signals():

    def add(collection, ticker, volume, pct_sl):
        collection = db[collection]
        new_signal = {"Ticker":ticker, "Volume":volume, "SL":pct_sl }
        data = collection.insert_one(new_signal)
        return data

    def find_all(collection):
        tickers = {}
        collection = db[collection]
        data = collection.find({})
        for dt in data:
            tickers[dt["Ticker"]] = [dt["Volume"], dt["SL"]] #{"BTCUSDT":[5646548654, -3.5]}
        return tickers

    def clear_all(collection):
        collection = db[collection]
        collection.delete_many({}) 

class Orders():
    def save_buy_order(collection, symbol, orderId, origQty, cummulativeQuoteQty, avgPrice):
        collection = db[collection]
        new_order = {"Symbol":symbol, "OrderId":orderId, "Quantity":origQty, "Amount":cummulativeQuoteQty,
                        "BuyPrice":avgPrice}
        data = collection.insert_one(new_order)
        return data

    def save_oco_order(collection, symbol, orderId, origQty, take_profit, stop_limit, trigger_price):
        collection = db[collection]
        new_order = {"Symbol":symbol, "OrderId":orderId, "Quantity":origQty,
                        "TP":take_profit, "SL":stop_limit, "Trigger":trigger_price}
        data = collection.insert_one(new_order)
        return data 