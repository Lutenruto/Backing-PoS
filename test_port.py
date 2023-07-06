import requests

base_url = 'http://10.33.2.123:{}/ping'


def test_ping_ports():
    for port in range(1024, 65536):
        url = base_url.format(port)
        response = requests.get(url)
        if response.text.lower() == 'pong':
            print('Réponse "pong" reçue sur le port :', port)
            break


test_ping_ports()
