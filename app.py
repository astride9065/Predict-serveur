from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    return "Serveur Astronaut en ligne"

@app.route("/scrape")
def scrape():
    url = "https://1win.com.ci/casino/play/100hp_100hpgaming_astronaut"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Exemple : récupérer le titre de la page
        title = soup.title.string if soup.title else "Pas de titre"

        return jsonify({"status": "ok", "title": title})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
