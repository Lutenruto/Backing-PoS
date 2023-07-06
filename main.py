import requests
from test_port import main as find_port

base_url = 'http://{}:{}'

ip_address = '10.33.2.123'
user = 'Lutenruto'
secret = None
port = None
level = None
points = None


def find_ports():
    global port
    port = find_port()
    if port is not None:
        print('Port trouvé :', port)
    else:
        print('Aucune réponse "pong" reçue sur les ports testés.')


def signup_request():
    signup_url = base_url.format(ip_address, port) + '/signup'
    signup_data = {'User': user}
    response = requests.post(signup_url, json=signup_data)
    print('POST /signup - Statut de la réponse:', response.status_code)
    print('Contenu de la réponse:', response.text)


def check_request():
    check_url = base_url.format(ip_address, port) + '/check'
    check_data = {'User': user}
    response = requests.post(check_url, json=check_data)
    print('POST /check - Statut de la réponse:', response.status_code)
    print('Contenu de la réponse:', response.text)


def secret_request():
    global secret
    secret_url = base_url.format(ip_address, port) + '/secret'
    secret_data = {'User': user}
    response = requests.post(secret_url, json=secret_data)
    print('POST /secret - Statut de la réponse:', response.status_code)
    print('Contenu de la réponse:', response.text)
    secret = response.text.split(':')[-1].strip()


def get_level():
    global level
    level_url = base_url.format(ip_address, port) + '/getLevel'
    level_data = {'User': user, 'Secret': secret}
    response = requests.post(level_url, json=level_data)
    print('POST /getLevel - Statut de la réponse:', response.status_code)
    print('Contenu de la réponse:', response.text)
    level = (int(response.text.split(':')[-1].strip())+2)
    print('Level :', level)


def get_user_points():
    global points
    points_url = base_url.format(ip_address, port) + '/getUserPoints'
    points_data = {'User': user, 'Secret': secret}
    response = requests.post(points_url, json=points_data)
    print('POST /getUserPoints - Statut de la réponse:', response.status_code)
    print('Contenu de la réponse:', response.text)
    parts = response.text.split(':')[-1].strip()
    points = (int(parts.split('\n')[-1].strip())-1)


def get_challenge():
    challenge_url = base_url.format(ip_address, port) + '/getChallenge'
    points_data = {'User': user, 'Secret': secret}
    response = requests.post(challenge_url, json=points_data)
    print('POST /getChallenge - Statut de la réponse:', response.status_code)
    print('Contenu de la réponse:', response.text)


def submit_challenge():
    print('Level :', level)
    submit_url = base_url.format(ip_address, port) + '/submitChallenge'
    points_data = {
        'User': user,
        'Secret': secret,
        'Content': {
            'Level': level,
            'Challenge': {
                'Username': user,
                'Secret': secret,
                'Points': points,
            },
            'Protocol': "SHA-1",
            'SecretKey': "Il n'y a que les imbéciles qui ne changent pas d'avis.",
        }
    }
    response = requests.post(submit_url, json=points_data)
    print('POST /submitChallenge - Statut de la réponse:', response.status_code)
    print('Contenu de la réponse:', response.text)


def get_hint():
    hint_url = base_url.format(ip_address, port) + '/getHint'
    points_data = {'User': user, 'Secret': secret}
    response = requests.post(hint_url, json=points_data)
    print('POST /getHint - Statut de la réponse:', response.status_code)
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
        # get_challenge()
        # get_hint()
        submit_challenge()
    else:
        print('Aucune réponse "pong" reçue sur les ports testés.')


if __name__ == '__main__':
    main()
