import os
import time
import threading
import requests
from flask import Flask

app = Flask(__name__)

TOKEN = "9107185721:AAGabfLENoeAd2aMWxwPOF6Vg7vxgeLw7MU"
URL = f"https://api.telegram.org/bot{TOKEN}/"

@app.route('/')
def home():
    return "Boti i futbollit është aktiv!"

def run_bot():
    last_id = None
    print("Boti u ndez në sfond!")
    while True:
        try:
            res = requests.get(URL + "getUpdates", params={"offset": last_id, "timeout": 30}).json()
            for update in res.get("result", []):
                last_id = update["update_id"] + 1
                if "message" in update and "text" in update["message"]:
                    chat_id = update["message"]["chat"]["id"]
                    text = update["message"]["text"]
                    
                    if text == "/start":
                        requests.get(URL + "sendMessage", params={
                            "chat_id": chat_id, 
                            "text": "👋 Përshëndetje! Boti i futbollit është aktiv në Render!"
                        })
                    else:
                        requests.get(URL + "sendMessage", params={
                            "chat_id": chat_id, 
                            "text": "Mesazhi u mor me sukses!"
                        })
        except Exception as e:
            print("Gabim:", e)
        time.sleep(2)

if __name__ == '__main__':
    t = threading.Thread(target=run_bot)
    t.daemon = True
    t.start()
    
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
