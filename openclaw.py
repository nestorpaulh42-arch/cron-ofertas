import requests
import os

TOKEN = os.getenv("8780839698:AAG4Xh6OfFeDinsAfm9anoGm8U_9_n6s4Z4")
CHAT_ID = os.getenv("-1003749638020")

print("TOKEN:", TOKEN)
print("CHAT_ID:", CHAT_ID)

def enviar(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    r = requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
    print("RESPUESTA TELEGRAM:", r.text)

def main():
    if not TOKEN or not CHAT_ID:
        print("❌ VARIABLES VACÍAS")
        return

    mensaje = "🚀 MENSAJE DE PRUEBA DESDE GITHUB"
    enviar(mensaje)

if __name__ == "__main__":
    main()
