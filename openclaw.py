import requests
from bs4 import BeautifulSoup
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def enviar(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    r = requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
    print("RESPUESTA TELEGRAM:", r.text)

def main():
    mensaje = "🚀 PRUEBA FUNCIONANDO DESDE GITHUB"

    try:
        r = requests.get("https://www.google.com")
        mensaje += "\n\nInternet OK ✅"

    except Exception as e:
        mensaje = f"❌ ERROR INTERNET:\n{str(e)}"

    enviar(mensaje)

if __name__ == "__main__":
    main()
