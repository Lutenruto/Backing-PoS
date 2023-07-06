import sys
import requests

base_url = 'http://10.33.2.123:3210'


# Requête GET à /ping
def ping_request():
    ping_url = base_url + '/ping'
    response = requests.get(ping_url)
    print('GET /ping - Statut de la réponse:', response.status_code)
    print('Contenu de la réponse:', response.text)


# Requête POST à /signup
def signup_request():
    signup_url = base_url + '/signup'
    signup_data = {'User': 'Lutenruto'}
    response = requests.post(signup_url, json=signup_data)
    print('POST /signup - Statut de la réponse:', response.status_code)
    print('Contenu de la réponse:', response.text)


# Requête POST à /check
def check_request():
    check_url = base_url + '/check'
    check_data = {'User': 'Lutenruto'}
    response = requests.post(check_url, json=check_data)
    print('POST /check - Statut de la réponse:', response.status_code)
    print('Contenu de la réponse:', response.text)


# Requête POST à /secret
def secret_request():
    secret_url = base_url + '/secret'
    secret_data = {'User': 'Lutenruto'}
    response = requests.post(secret_url, json=secret_data)
    print('POST /secret - Statut de la réponse:', response.status_code)
    print('Contenu de la réponse:', response.text)


# Vérification des arguments de ligne de commande et exécution de la requête appropriée
if len(sys.argv) < 2:
    print("Veuillez spécifier une requête (ping, signup, check, secret).")
else:
    command = sys.argv[1]
    if command == 'ping':
        ping_request()
    elif command == 'signup':
        signup_request()
    elif command == 'check':
        check_request()
    elif command == 'secret':
        secret_request()
    else:
        print("Requête invalide. Veuillez spécifier une requête valide (ping, signup, check, secret).")
