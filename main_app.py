from binance_client import client
from database import Status
import datetime as dt
import time
import time_server as ts
import telegram_msg as Tb
import requests

while True:

 Pkey = 'wPwRh8oHCGhpLMF9zdYRWFrHxniROVX2A9XQmLTnIFbVCqv8asr9rnFuVvcf7vlM'
 Skey = 'KqgHRiQfZJloSG4ZId7ahPiH62Ql6q5PovGJwuJ8m24kL1QOF8qCmRswnDdaCxTZ'

 client = Client(api_key=Pkey, api_secret=Skey) 

 base_url = "https://api.binance.com"
 endpoint = "/api/v1/ping"
 Binance = base_url + endpoint

 r = requests.get(Binance)
 print(r.json(),"Binance server is : Connected"),Tb.send_message("Binance server is : Connected")

 def time_now():
  time = dt.datetime.now()
  time = time.strftime("%H:%M:%S    //   %d-%m-%Y") #10:42:30   //   01-03-2021
  return time

 x = 0
 y = 0
 #connection = "OK"

 while True:
  #try:
    ts.server_tm()
    stat = Status.find_status(collection = "Status")
    while "ON" in stat:
      ts.server_tm()
      if x == 0:
        y = 0
        print("System activated at :", time_now()),Tb.send_message("System and Bot are activated Now")

        x = x+1

      stat = Status.find_status(collection = "Status")
    if y == 0:
      x = 0
      print("System disactivated at :", time_now()),Tb.send_message("System and Bot are disactivated Now")
      y = y+1
  #except: 
     #pass 

    time.sleep(2)   
 
 
