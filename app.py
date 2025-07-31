from flask import Flask, request, jsonify
from google_sheets_logger import log_reservation
from config import WEBHOOK_SECRET
import datetime

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return "✅ Tock-to-Corksy Sync is live."

@app.route('/test-log', methods=['POST'])
def test_log():
    data = request.json or {
        "first_name": "Test",
        "last_name": "Guest",
        "email": "test@example.com",
        "phone": "123-456-7890",
        "reservation_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    log_reservation(data['first_name'], data['last_name'], data['email'], data['phone'], data['reservation_time'])
    return "Logged test guest."

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('Authorization') != WEBHOOK_SECRET:
        return "Unauthorized", 401

    payload = request.json
    try:
        guest = payload["guest"]
        first_name = guest.get("first_name", "")
        last_name = guest.get("last_name", "")
        email = guest.get("email", "")
        phone = guest.get("phone_number", "")
        reservation_time = payload.get("reservation_time", "")

        log_reservation(first_name, last_name, email, phone, reservation_time)
        return "Reservation logged", 200
    except Exception as e:
        print("Error processing webhook:", e)
        return "Error", 500
