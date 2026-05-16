import sys, socket, re
from tqdm import tqdm

def test_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        s.connect_ex((ip, port))
        s.close()
    except Exception as e:
        pass
        return e

def scan(ip):
    ipv4_pattern = "^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    if not re.match(ipv4_pattern, ip):
        print('Ungültige IP-Adresse.')
    else:
        open_ports = []
        for port in tqdm(range(1, 65536), desc=f"[+] Starte Scan von {ip} ..."):
            if test_port(ip, port) == 0:
                open_ports.append(port)
        if open_ports:
            print(f'Es wurden {len(open_ports)} offene Ports gefunden: {open_ports}')
        else:
            print('Es wurden keine offenen Ports gefunden.')

if __name__ == '__main__':
    ip = sys.argv[1]
    scan(ip)