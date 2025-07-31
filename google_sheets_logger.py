import gspread
import json
import base64
import datetime
from oauth2client.service_account import ServiceAccountCredentials
from config import GOOGLE_CREDENTIALS_JSON, SHEET_ID

def get_sheet():
    creds_dict = json.loads(base64.b64decode(GOOGLE_CREDENTIALS_JSON))
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SHEET_ID).sheet1
    return sheet

def log_reservation(first_name, last_name, email, phone, time):
    sheet = get_sheet()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [first_name, last_name, email, phone, time, now]
    sheet.append_row(row)
