# 🔐 CipherNest — Text Encryption & Decryption Tool

A web-based text encryption and decryption application built with **Python, Flask, and Cryptography**. CipherNest provides a simple, interactive interface for encrypting and decrypting text using Fernet encryption and the Caesar Cipher.

## ✨ Features

- 🔒 **Fernet Encryption:** Encrypt and decrypt text using the Fernet symmetric encryption scheme.
- 🔤 **Caesar Cipher:** Perform classical encryption and decryption using a configurable shift value.
- ⚡ **Interactive Visualizer:** View dynamic visual feedback while working with encryption and decryption.
- 📋 **Copy Results:** Copy the generated output directly from the interface.
- 📥 **Download Results:** Download the processed text.
- 🎨 **Modern UI:** A dark, cybersecurity-inspired interface with responsive styling.
- 🛡️ **Simple and Beginner-Friendly:** Explore basic encryption concepts through a hands-on web application.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Web framework and routing |
| HTML5 | Page structure |
| CSS3 | Styling and responsive UI |
| JavaScript | Interactive visualizer and UI behavior |
| Cryptography | Fernet encryption and decryption |

## 🔑 Encryption Methods

### 1. Fernet Encryption

Fernet provides authenticated symmetric encryption. It uses a secret key to encrypt and decrypt data, helping protect confidentiality and detect tampering.

**Note:** Keep the Fernet key secure. Anyone with the key can decrypt data encrypted with it.

### 2. Caesar Cipher

The Caesar Cipher is a classical substitution cipher that shifts letters by a specified number of positions in the alphabet.

For example, with a shift of 3:

- A → D
- B → E
- C → F

This method is included for educational purposes and is **not secure for protecting sensitive information**.

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or a compatible Python version
- pip
- Git

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

Replace the URL and folder name with your actual repository details.

### 2. Create a Virtual Environment

**Windows:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```cmd
venv\Scripts\activate.bat
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Open the local URL displayed in your terminal, typically:

```text
http://127.0.0.1:5000
```

## 📖 How to Use

1. Open the application in your browser.
2. Enter the text you want to process.
3. Select Fernet or Caesar Cipher.
4. Enter a shift value if using Caesar Cipher.
5. Choose Encrypt or Decrypt.
6. View the result in the output panel.
7. Copy or download the processed text.

## 🎯 Project Objectives

- Understand the fundamentals of encryption and decryption.
- Explore the difference between classical and modern symmetric encryption.
- Build a Python web application using Flask.
- Practice frontend and backend integration.
- Improve the user experience through interactive visual feedback.

## 🔮 Future Improvements

- File encryption and decryption.
- Secure key management.
- Additional classical and modern encryption demonstrations.
- Improved input validation and error handling.
- Automated testing for encryption and decryption workflows.

## ⚠️ Security Disclaimer

This project is intended for **educational purposes and learning about cryptographic concepts**. Do not use the Caesar Cipher to protect sensitive information. Before using this application for real-world confidential data, review its key management, deployment configuration, input handling, and security practices.


⭐ If you find this project interesting, consider starring the repository!
