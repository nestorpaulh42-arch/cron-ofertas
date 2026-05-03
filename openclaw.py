import requests
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("=== DEBUG ===")
print("TOKEN:", TOKEN)
print("CHAT_ID:", CHAT_ID)

def enviar(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    r = requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
    print("RESPUESTA TELEGRAM:", r.text)

def main():
    if not TOKEN or not CHAT_ID:
        print("❌ ERROR: variables vacías")
        return

    print("✅ Variables OK")
    enviar("🚀 MENSAJE DESDE GITHUB FUNCIONANDO")

if __name__ == "__main__":
    main()
