from get_data import get_klines
import talib as ta
import tickers as tkr
from database import Signals
import threading
from datetime import datetime

interval = "15m"
depth = "50 hours ago UTC+1"
ema_used = [50, 100]

def find_engulging(series):
    for i in series.index:
        if series[i] == 100:
            return i

def engulfing_strgy(tickers, num):
    for ticker in tickers:
        try:
            df = get_klines(pair = ticker, interval = interval, depth = depth)
            if not df.empty:
                for i in ema_used:
                    df["EMA_"+str(i)] = ta.EMA(df["Close"], timeperiod = i)
                df_2 = df.tail(5)
                engulfing = ta.CDLENGULFING(df_2["Open"], df_2["High"], df_2["Low"], df_2["Close"])
                last_index = find_engulging(series = engulfing)

                if bool(last_index):
                    close_price = float(df["Close"][last_index])
                    volume = float(df["Volume"][last_index])
                    volume = round(volume, 2)
                    ema_50 = float(df["EMA_50"][last_index])
                    ema_100 = float(df["EMA_100"][last_index])
                    low_price = float(df["Low"][last_index])
                    pct_change = ((low_price *100) / close_price) - 100
                    pct_change = round(pct_change, 2)
                    now = datetime.now()
                    now = now.minute
                    candle_time = last_index.minute

                    if (close_price > ema_50 or close_price > ema_100) and ema_50 > ema_100 and pct_change > -4 and (candle_time == now - 15 ):
                     Signals.add(collection = "Signals", ticker = ticker, volume = volume, pct_sl = pct_change)
        except:
            pass
    Signals.add(collection = "Signals", ticker = "End_"+str(num), volume = 0, pct_sl = 0) 
    print("End_", num) 