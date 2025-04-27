import time
import requests
from flask import Flask
from threading import Thread

# Cria o servidor Flask
app = Flask('')


@app.route('/')
def home():
    return "Pinger Online!"


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()


# Ativa o servidor web
keep_alive()

# URL do seu site no Render (para o pinger funcionar)
url = 'https://mateusfelipeborges.com'  # <-- Ajuste para o seu link real

# Loop infinito para pingar o site
while True:
    try:
        response = requests.get(url)
        print(f'[{time.ctime()}] Ping enviado! Status: {response.status_code}')
    except Exception as e:
        print(f'[{time.ctime()}] Erro ao pingar: {e}')

    # Espera 60 segundos (1 minuto)
    time.sleep(60)
