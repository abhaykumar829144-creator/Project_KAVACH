# 🛡️ Project KAVACH (Secure Satellite Communication System)

Project KAVACH is a Python-based cybersecurity project that simulates a secure, real-time communication network between a satellite and a ground station. It demonstrates practical implementations of network security, cryptography, and digital forensics.

## 🚀 Key Features

*   **AES-256 Encryption:** Satellite telemetry data is fully encrypted using the `cryptography.fernet` library before transmission.
*   **UDP Network Communication:** Fast and efficient data transmission over UDP sockets.
*   **Automated Alert System:** The ground station actively monitors incoming data and triggers critical warnings (e.g., Battery Low).
*   **Red Teaming (Packet Sniffing):** Includes a `hacker.py` script that attempts to intercept network traffic, demonstrating that raw encrypted payloads are unreadable without the symmetric key.
*   **Black Box Logging:** All incoming data and system alerts are permanently recorded in a `kavach_logs.txt` file with timestamps for digital forensic analysis.

## 💻 Tech Stack
*   **Language:** Python 3
*   **Libraries:** `socket`, `cryptography`, `json`, `datetime`, `random`, `time`
*   **Concepts:** Socket Programming, Symmetric Encryption, Network Sniffing, Log Management.

## 🛠️ How to Run Locally

1. Install the required cryptography library:
   `pip install cryptography`
2. Open three separate terminals.
3. Start the Satellite (Transmitter):
   `python satellite.py`
4. Start the Ground Station (Receiver & Logger):
   `python ground_station.py`
5. Test the Network Security (Hacker Terminal):
   `python hacker.py`
   