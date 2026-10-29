import os
import time
import requests

TOKEN = os.environ.get("TOKEN", "9107185721:AAGabfLENoeAd2aMWxwPOF6Vg7vxgeLw7MU")
URL = f"https://api.telegram.org/bot{TOKEN}/"

print("Boti u ndez në Render!")

def main():
    last_id = None
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
                            "text": "👋 Përshëndetje nga Render! Boti yt është aktiv 24/7!"
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
    main()
