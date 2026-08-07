import socket
import json
from datetime import datetime
from cryptography.fernet import Fernet

SECRET_KEY = b'G25eyEYwJK4N2--syib3k88rACPfU5VpOA18touQhoc='
cipher_suite = Fernet(SECRET_KEY)

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("Ground Station Radar & Black Box Logger Online!\n")

while True:
    data, addr = sock.recvfrom(1024) 
    try:
        asli_data = cipher_suite.decrypt(data)
        parsed_data = json.loads(asli_data.decode())
        
        print(f"[SUCCESS] REAL DATA: {parsed_data}")
        
        log_entry = f"[{datetime.now()}] {parsed_data}\n"
        with open("kavach_logs.txt", "a") as log_file:
            log_file.write(log_entry)
        
        if parsed_data["battery_percent"] < 90.0:
            print(">>> [CRITICAL WARNING] SATELLITE BATTERY LOW! <<<")
            with open("kavach_logs.txt", "a") as log_file:
                log_file.write(f"[{datetime.now()}] ALARM: BATTERY DROP DETECTED!\n")
                
    except Exception as e:
        print("[ALARM] Decryption Failed!")