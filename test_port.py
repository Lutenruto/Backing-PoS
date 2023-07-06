import requests
from requests.exceptions import Timeout
from concurrent.futures import ThreadPoolExecutor

base_url = 'http://{ip}:{port}/ping'
ip_addresses = ['10.33.2.123']  # Ajoutez ici les adresses IP à tester
stop_execution = False


def test_ping_ports(ip_address, start_port, end_port):
    global stop_execution
    for port in range(start_port, end_port + 1):
        if stop_execution:
            return
        url = base_url.format(ip=ip_address, port=port)
        try:
            response = requests.get(url, timeout=0.02)
            if response.status_code == 200 and response.text.lower() == 'pong':
                print('Réponse 200 "pong" reçue sur le port :', port)
                stop_execution = True
                return port
        except Timeout:
            pass


def main():
    num_workers = 100
    port_range = 4096 - 1024 + 1
    ports_per_worker = port_range // num_workers

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = []

        for ip_address in ip_addresses:
            for i in range(num_workers):
                start_port = 1024 + i * ports_per_worker
                end_port = start_port + ports_per_worker - 1

                if i == num_workers - 1:
                    end_port = 4096

                future = executor.submit(test_ping_ports, ip_address, start_port, end_port)
                futures.append(future)

        for future in futures:
            port = future.result()
            if port is not None:
                return port

    return None


if __name__ == '__main__':
    main()
