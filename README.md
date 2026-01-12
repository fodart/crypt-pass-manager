# crypt pass manager

A robust command-line tool to store and manage your passwords securely. It uses industry-standard encryption to ensure your data stays private.

### Security Features
- **Master Authentication:** Passwords are never stored in plain text; only SHA-256 hashes are used for verification.
- **Strong Encryption:** Uses the `cryptography` (Fernet/AES) library for high-level data protection.
- **Secure Input:** Utilizes `getpass` to hide password typing in the terminal.

### Installation & Usage
1. Install dependencies: `pip install cryptography`
2. Run the script: `python manager.py`
3. Follow the prompts to add or retrieve your credentials.

### Tech Stack
- **Python 3.x**
- **Libraries:** `cryptography`, `hashlib`, `json`, `base64`.
