#  Tock-to-Corksy Sync

This project helps Amavi Cellars save time and reduce errors by automatically logging new reservations from **Tock** into a **Google Sheet**, so staff don’t need to manually retype them into Corksy. It runs in the background and just works.

---

##  What It Does

- Listens for new Tock reservations via webhook.
- Pulls the **first name**, **last name**, **email**, and **phone number**.
- Adds that data to a connected Google Sheet.
- The sheet can be used to create customers in Corksy manually (for now).
- Fully hosted on Render — no maintenance required.

---

##  Why We Built It

Currently, staff manually copy reservation info from Tock into Corksy every morning, which is time-consuming and error-prone. This service automates that first step, creating a central list of reservations in a Google Sheet for the day. Corksy says they are working on an official integration — this tool fills the gap in the meantime.

---

##  Hosting & Deployment

This app is hosted on [Render.com](https://render.com), a cloud platform that keeps it running 24/7. When a new reservation is made, Tock sends a POST request to our unique Render URL. That data is processed and written to the next row in our connected Google Sheet.

Whenever the code is updated on GitHub, Render redeploys the app automatically.

---

## How It Works 

1. Customer makes a reservation through Tock.
2. Tock sends the reservation info to our webhook (hosted on Render).
3. The app extracts the name, email, and phone number.
4. The info is added to a designated Google Sheet.

---

##  Example

A new Tock reservation comes in:

##  Example

A new Tock reservation comes in:

Name: John Smith
Email: john@example.com
Phone: 555-123-4567


It is logged in the Google Sheet like this:

John | Smith | john@example.com | 555-123-4567

---

##  Technical Details (for Developers or IT)

- **Language**: Python 3
- **Framework**: Flask
- **Hosting**: Render.com
- **Logging Target**: Google Sheet (via Google Sheets API)
- **Auth**: Uses a base64-encoded Google service account key stored securely as an environment variable
- **Webhook Endpoint**: Hosted on Render, accepts `POST` requests
- **Webhook Security**: Optional secret header token (`Authorization: Bearer ...`) to validate incoming requests
- **Deployment**: Render redeploys automatically when new code is pushed to GitHub

### Environment Variables (in Render)

- `GCP_KEY_BASE64`: Your Google Sheets service account key, encoded in base64
- `WEBHOOK_SECRET`: (Optional) Secret token to authorize webhook requests from Tock

---

## Project Structure

- `app.py`: The Flask web server and webhook handler
- `google_sheets_logger.py`: Logic for writing reservation data into the Google Sheet
- `config.py`: Handles loading and decoding environment variables
- `render.yaml`: Render deployment config (optional if deploying manually)
- `requirements.txt`: Python dependencies
- `README.md`: Project documentation (this file)

---

## For Future Maintainers

- Make sure the service account email (from the Google Cloud console) has **Editor** access to the target Google Sheet.
- If you change the service account key, update the `GCP_KEY_BASE64` variable in Render.
- Logs and error messages can be viewed from the **Logs** tab in the Render dashboard.
- You can test the webhook manually using `curl`:

curl -X POST https://your-render-url/webhook
-H "Content-Type: application/json"
-H "Authorization: Bearer your-secret"
-d '{
"first_name": "Alice",
"last_name": "Johnson",
"email": "alice@example.com",
"phone": "555-123-9876"
}'


- If Corksy releases an API in the future, a new script (e.g. `corksy_client.py`) can be added to send data directly to them instead of or alongside the Google Sheet.

---

## 🧾 License

MIT License — free to use, modify, or expand.
