# Tock to Corksy Sync 🥂

This webhook service listens for Tock reservations and logs guest data to a Google Sheet. It’s ready for future integration with Corksy if an API becomes available.

## Features
- Secure webhook listener
- Google Sheets logging via service account
- Corksy API stub for future use

## Deployment
1. Clone the repo
2. Set environment variables:
   - `WEBHOOK_SECRET`
   - `GOOGLE_CREDENTIALS_JSON` (base64-encoded JSON key)
   - `SHEET_ID`
3. Deploy to Render or run locally:
   ```bash
   gunicorn app:app


## Dev Tools
/ping – Health check
/test-log – Manually test logging

Maintainer
Built by @grantdidway. See docs/handoff.md for transfer instructions.