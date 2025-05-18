# 🧙‍♂️ Curse and Decryptionite (For Learning Purposes Only)

## ⚠️ Disclaimer

**FOR LEARNING PURPOSES ONLY. THIS CODE IS ONLY TO DISPLAY HOW THIS CERTAIN MALWARE WORKS.**

This repository contains a pair of Python scripts designed to demonstrate basic encryption and decryption using the `cryptography` library. The purpose of these scripts is to illustrate how ransomware-like functionality can be implemented and mitigated in a controlled, educational setting.

🚫 **Do not use this code for malicious purposes. Unauthorized use may violate laws and result in severe penalties.**

---

## 🛠️ Overview

- **`curse.py`:** Encrypts files in the directory using a generated key and displays a fictional ransom note.  
- **`decryptionite.py`:** Decrypts the files using the generated key, restoring them to their original state.

---

## ⚡ How It Works

1. The `curse.py` script searches the current directory for files, excluding itself, the decryption script, and the key file.  
2. It generates a unique encryption key using `Fernet.generate_key()` and saves it to `thekey.key`.  
3. The script then encrypts each file's contents using the key and writes a fictional ransom note, simulating ransomware behavior.  
4. The `decryptionite.py` script reads the key from `thekey.key` and decrypts the files, restoring them to their original state.

---

## 🚀 Usage

### 1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>

2. Install dependencies:
bash
Copy
Edit
pip install cryptography

3. Run the encryption script:
bash
Copy
Edit
python curse.py

4. Run the decryption script:
bash
Copy
Edit
python decryptionite.py

🛑 Important Notes
This code is intended solely for educational purposes to demonstrate how ransomware functions at a basic level.

Use in a controlled environment only. Do not run on sensitive or production data.

The author is not responsible for any misuse of this code.

📜 License
MIT License

Copyright (c) 2025 jcodes101
