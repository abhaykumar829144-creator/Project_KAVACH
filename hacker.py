import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("HACKER TERMINAL: Sniffing Network for Satellite Data...\n")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"[*] DATA INTERCEPTED FROM: {addr}")
    print(f"[!] RAW ENCRYPTED PAYLOAD: {data}")
    print("[-] DECRYPTION ATTEMPT: FAILED (No AES-256 Key)\n")