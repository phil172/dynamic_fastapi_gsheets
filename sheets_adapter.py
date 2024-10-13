import gspread
from google.oauth2.service_account import Credentials
import requests

class GoogleSheetsServiceAccountAdapter:
    def __init__(self, creds_file, sheet_id, sheet_name):
        self.creds = Credentials.from_service_account_file(
            creds_file, 
            scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"]
        )
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open_by_key(sheet_id).worksheet(sheet_name)

    def get_sheet_data_as_json(self, expected_headers=None):
        try:
            # This returns a list of dictionaries (not a JSON string)
            data = self.sheet.get_all_records(expected_headers=expected_headers)
            return data  # Return the data directly as a list of dicts
        except gspread.exceptions.GSpreadException as err:
            print(f"GSpread error occurred: {err}")
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")

# Usage example:
if __name__ == "__main__":
    CREDS_FILE = 'path_to_your_service_account_credentials.json'
    SHEET_ID = 'your_google_sheet_id'
    SHEET_NAME = 'Sheet1'

    sheet_adapter = GoogleSheetsServiceAccountAdapter(CREDS_FILE, SHEET_ID, SHEET_NAME)
    sheet_data = sheet_adapter.get_sheet_data_as_json(expected_headers=["route", "method", "body", "handler"])
    
    # sheet_data is already a list of dictionaries, no need to call json.loads()
    print(sheet_data)