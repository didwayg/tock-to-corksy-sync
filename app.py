from flask import Flask, request, jsonify
import os
import base64
import json
import gspread
from google.oauth2.service_account import Credentials

app = Flask(__name__)

@app.route("/ping")
def ping():
    return "✅ Tock-to-Corksy Sync is live."

@app.route("/webhook", methods=["POST"])
def handle_webhook():
    data = request.get_json()
    print("[DEBUG] Webhook received:", data)

    # Auth check
    auth_header = request.headers.get("Authorization", "")
    expected = f"Bearer {os.getenv('WEBHOOK_SECRET', '')}"
    if auth_header != expected:
        return jsonify({"error": "Unauthorized"}), 401

    # Extract fields
    name = f"{data.get('first_name', '')} {data.get('last_name', '')}".strip()
    email = data.get("email")
    phone = data.get("phone")

    if not email:
        return jsonify({"error": "Missing email"}), 400

    try:
        sheet = get_gsheet()
        sheet.append_row([name, email, phone])
        return jsonify({"status": "added"}), 200
    except Exception as e:
        print("[ERROR]", str(e))
        return jsonify({"error": str(e)}), 500

def get_gsheet():
    key_b64 = os.getenv("GOOGLE_CREDENTIALS_JSON")
    json_key = base64.b64decode(key_b64).decode("utf-8")
    creds_dict = json.loads(json_key)

    creds = Credentials.from_service_account_info(
        creds_dict,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )

    client = gspread.authorize(creds)
    sheet_id = os.getenv("SHEET_ID")
    return client.open_by_key(sheet_id).sheet1
