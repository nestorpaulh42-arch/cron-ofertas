import requests
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def enviar(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    r = requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
    print("RESPUESTA:", r.text)

def main():
    mensaje = "🚀 FUNCIONANDO DESDE GITHUB"
    enviar(mensaje)

if __name__ == "__main__":
    main()
