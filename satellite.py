import json
import random
import time
import socket
from cryptography.fernet import Fernet

SECRET_KEY = b'G25eyEYwJK4N2--syib3k88rACPfU5VpOA18touQhoc='
cipher_suite = Fernet(SECRET_KEY)

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Satellite Transmitting over UDP Network...\n")

def generate_telemetry():
    data = {
        "satellite_id": "KAVACH-SAT-01",
        "timestamp": round(time.time(), 2),
        "altitude_km": round(random.uniform(390.0, 410.0), 2),
        "temperature_c": round(random.uniform(-50.0, 80.0), 2),
        "battery_percent": round(random.uniform(85.0, 100.0), 2)
    }
    raw_json = json.dumps(data)
    return cipher_suite.encrypt(raw_json.encode())

while True:
    locked_packet = generate_telemetry()
    sock.sendto(locked_packet, (UDP_IP, UDP_PORT))
    print(f"[SENT TO SPACE] -> {locked_packet}")
    time.sleep(2)