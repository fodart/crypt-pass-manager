import hashlib
import json
import os
import base64
from cryptography.fernet import Fernet
from getpass import getpass

def generate_key(password: str) -> bytes:
    hash_key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hash_key)

example = {
    "user": {"is_master_password_set": False, "master_password": ""},
    "services": {}
}

filename = "manager.json"
if not os.path.exists(filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(example, f, indent=2)

with open(filename, "r", encoding="utf-8") as f:
    data = json.load(f)

master_input = getpass("Enter your master password: ")
input_hash = hashlib.sha256(master_input.encode()).hexdigest()

if not data["user"]["is_master_password_set"]:
    data["user"]["master_password"] = input_hash
    data["user"]["is_master_password_set"] = True
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("Master password set!")
else:
    if data["user"]["master_password"] != input_hash:
        print("Invalid Password!")
        exit()

cipher = Fernet(generate_key(master_input))

while True:
    action = input("\n1 - See password | 2 - Add service | 3 - Exit: ")

    if action == "1":
        service = input("Enter service name: ")
        if service in data["services"]:
            encrypted_pass = data["services"][service].encode()
            decrypted = cipher.decrypt(encrypted_pass).decode()
            print(f"Password for {service}: {decrypted}")
        else:
            print("Service not found.")

    elif action == "2":
        service = input("Enter service name: ")
        service_pass = getpass("Enter password for service: ")
        
        encrypted = cipher.encrypt(service_pass.encode()).decode()
        data["services"][service] = encrypted
        
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"Service '{service}' added!")

    elif action == "3":
        break