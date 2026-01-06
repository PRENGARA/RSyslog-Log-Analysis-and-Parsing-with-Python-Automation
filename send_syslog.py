import socket
import time

def send_syslog(filename, host, protocol):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return
    protocol = protocol.upper()
    if protocol not in ['TCP', 'UDP']:
        print("Invalid protocol specified")
        return
    port = 514
    if protocol == 'UDP':
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for line in lines:
            message = line.strip().encode()
            sock.sendto(message, (host, port))
            print(f"[UDP] Sent: {message.decode()}")
            time.sleep(1)
        sock.close()
    elif protocol == 'TCP':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((host, port))
            for line in lines:
                message = line.strip().encode() + b'\n'
                sock.sendall(message)
                print(f"[TCP] Sent: {message.decode().strip()}")
                time.sleep(1)
        except ConnectionRefusedError:
            print("Connection refused – check if rsyslog TCP input is enabled.")
        finally:
            sock.close()
if __name__ == "__main__":
    send_syslog('system2.log', '127.0.0.1', 'UDP')
