import binance.client
from binance.client import Client
import requests
import telegram_msg as Tb


Pkey = 'wPwRh8oHCGhpLMF9zdYRWFrHxniROVX2A9XQmLTnIFbVCqv8asr9rnFuVvcf7vlM'
Skey = 'KqgHRiQfZJloSG4ZId7ahPiH62Ql6q5PovGJwuJ8m24kL1QOF8qCmRswnDdaCxTZ'

client = Client(api_key=Pkey, api_secret=Skey) 

base_url = "https://api.binance.com"
endpoint = "/api/v1/ping"
Binance = base_url + endpoint

r = requests.get(Binance)

print(r.json(),"Binance server is : Connected"),Tb.send_message("Binance server is : Connected")
