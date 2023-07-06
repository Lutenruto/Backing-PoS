import requests
from test_port import main as find_port

base_url = 'http://{}:{}/ping'

ip_address = '10.33.2.123'
user = "Lutenruto"
secret = None
port = None


def find_ports():
    global port
    port = find_port()
    if port is not None:
        print('Port trouvé :', port)
    else:
        print('Aucune réponse "pong" reçue sur les ports testés.')


def signup_request():
    signup_url = base_url.format(ip_address, port) + '/signup'
    signup_data = {'User': user, 'Secret': secret}
    response = requests.post(signup_url, json=signup_data)
    print('POST /signup - Statut de la réponse:', response.status_code)
    print('Contenu de la réponse:', response.text)


def check_request():
    check_url = base_url.format(ip_address, port) + '/check'
    check_data = {'User': user, 'Secret': secret}
    response = requests.post(check_url, json=check_data)
    print('POST /check - Statut de la réponse:', response.status_code)
    print('Contenu de la réponse:', response.text)


def secret_request():
    global secret
    secret_url = base_url.format(ip_address, port) + '/secret'
    secret_data = {'User': user, 'Secret': secret}
    response = requests.post(secret_url, json=secret_data)
    print('POST /secret - Statut de la réponse:', response.status_code)
    print('Contenu de la réponse:', response.text)
    secret = response.text.split(':')[-1].strip()


def get_level():
    level_url = base_url.format(ip_address, port) + '/getLevel'
    level_data = {'User': user, 'Secret': secret}
    response = requests.post(level_url, json=level_data)
    print('POST /getLevel - Statut de la réponse:', response.status_code)
    print('Contenu de la réponse:', response.text)


def get_user_points():
    points_url = base_url.format(ip_address, port) + '/getUserPoints'
    points_data = {'User': user, 'Secret': secret}
    response = requests.post(points_url, json=points_data)
    print('POST /getUserPoints - Statut de la réponse:', response.status_code)
    print('Contenu de la réponse:', response.text)


def main():
    global port
    find_ports()
    if port is not None:
        signup_request()
        check_request()
        secret_request()
        get_level()
        get_user_points()
    else:
        print('Aucune réponse "pong" reçue sur les ports testés.')


if __name__ == '__main__':
    main()
