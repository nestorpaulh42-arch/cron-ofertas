import requests
from bs4 import BeautifulSoup
import os

# 🔐 Variables desde GitHub Secrets
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

KEYWORDS = ["practicante", "jr", "junior", "trainee", "asistente"]

FUENTES = {
    "LIMA": [
        "https://www.practicas.pe/resultados-busqueda.php?q=ingenieria+civil&dep=15",
        "https://pe.computrabajo.com/trabajo-de-practicante-ingenieria-civil-en-lima",
    ],
    "AREQUIPA": [
        "https://www.practicas.pe/resultados-busqueda.php?q=ingenieria+civil&dep=3",
        "https://pe.computrabajo.com/trabajo-de-practicante-ingenieria-civil-en-arequipa",
    ],
}

def enviar(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def contiene_keyword(texto):
    texto = texto.lower()
    return any(k in texto for k in KEYWORDS)

def scrape(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        return []

    soup = BeautifulSoup(r.text, "html.parser")
    enlaces = soup.find_all("a")

    resultados = []

    for a in enlaces:
        titulo = a.text.strip()

        if len(titulo) > 20 and contiene_keyword(titulo):
            link = a.get("href")
            if link and link.startswith("http"):
                resultados.append({
                    "titulo": titulo,
                    "link": link
                })

    return resultados[:5]

def main():
    mensaje = "🚀 PRUEBA DESDE GITHUB FUNCIONANDO\n\n"
    total = 0

    for ciudad, urls in FUENTES.items():
        for url in urls:
            ofertas = scrape(url)

            if ofertas:
                mensaje += f"## {ciudad}\n"

                for i, o in enumerate(ofertas, 1):
                    mensaje += f"{i}. {o['titulo']}\n{o['link']}\n\n"
                    total += 1

    if total == 0:
        mensaje = "Sin nuevas ofertas hoy"

    enviar(mensaje)

if __name__ == "__main__":
    main()
