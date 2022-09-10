import requests 
 
def send_message(message): 
    bot_token = "5409782688:AAHyFXDkc0FGpsOspKeIt1C7bokYUnk0uYc" 
    bot_chatID =  "-1001626790498" 
    send_text = "https://api.telegram.org/bot"+bot_token+"/sendMessage?chat_id="+bot_chatID+"&parse_mode=Markdown&text="+message 
    response = requests.get(send_text) 
    return response.json()
