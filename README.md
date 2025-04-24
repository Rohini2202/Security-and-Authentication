# Flask Authentication & Security (MongoDB + HTTPS)

This project demonstrates how to implement **authentication**, **authorization**, **password hashing**, and **HTTPS** using Flask, MongoDB, and Flask-Security.

## Features

- User Registration and Login
- Role-based Authorization
- Password Hashing with Salting
- HTTPS (Secure Communication using SSL)
- MongoDB Integration using Flask-MongoEngine

## Tech Stack

- Python 3.10+
- Flask
- Flask-Security-Too
- Flask-MongoEngine
- pymongo
- MongoDB Atlas
- OpenSSL (for HTTPS cert generation)

## Project Structure
chatbot_auth/ ├── user_authentication.py # Main Flask app 
              ├── cert.pem # SSL Certificate (Generated locally) 
              ├── key.pem # SSL Private Key (Generated locally) 
              ├── requirements.txt # Dependencies 
              └── README.md # Project Documentation

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/chatbot_auth.git
cd chatbot_auth
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. 🔐 Generate HTTPS certs
If you don't have them yet, run:
```bash
openssl req -x509 -newkey rsa:4096 -nodes -keyout key.pem -out cert.pem -days 365
```
- Use localhost as Common Name when prompted

### 5. Setup MongoDB URI
Update your user_authentication.py with your MongoDB URI:

```python
app.config["MONGODB_SETTINGS"] = {
    "host": "your-mongodb-atlas-uri"
}
```
### 6. Run the app

```bash
python user_authentication.py
```
Open your browser and go to:
https://localhost:5000

## Notes
- Make sure MongoDB Atlas allows access from your current IP (or allow 0.0.0.0/0 during development).
- The SSL certificate is self-signed and may show warnings in browsers (ignore for local testing).
- Flask-Security-Too >= 5.0 requires your user model to include fs_uniquifier.





