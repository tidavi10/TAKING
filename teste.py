from flask import Flask
import requests

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def cep():

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(15507112))
    address_data = request.json()
    
    return address_data['logradouro']