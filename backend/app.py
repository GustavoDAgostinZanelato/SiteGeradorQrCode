from flask import Flask, request, jsonify
from flask_cors import CORS
from codigoQr import gerarQrCode
import requests

app = Flask(__name__)
CORS(app)

@app.route("/processarUrl", methods=["POST"])


def processarUrl():
    try:
        dados = request.get_json()
        urlRecebida = dados.get("url")
        
        if(verificarURL(urlRecebida)):
             gerarQrCode(urlRecebida)
             return jsonify({"mensagem": "QRcode gerado com sucesso!"})
        else:
             return jsonify({"mensagem": "URL inválida"})
    
    except Exception as e:
            print(f"Erro: {e}")
            return jsonify({"mensagem": "Erro ao processar a URL"}), 500


def verificarURL(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5) 
        return response.status_code < 400
    except requests.RequestException:
         return False
   
if __name__ == "__main__":
    app.run(debug=True)


    