import json
from fastapi import FastAPI, Request
from sheets_adapter import GoogleSheetsServiceAccountAdapter
from dotenv import load_dotenv
import os

load_dotenv()

CREDENTIAL_FILE = os.getenv('CREDENTIAL_FILE')
SHEET_ID = os.getenv('SHEET_ID')
SHEET_NAME = os.getenv('SHEET_NAME')

def get_config():
    sheet_adapter = GoogleSheetsServiceAccountAdapter(CREDENTIAL_FILE, SHEET_ID, SHEET_NAME)
    sheet_data_json = sheet_adapter.get_sheet_data_as_json(expected_headers=["route", "method", "body", "handler"])
    return sheet_data_json


app = FastAPI()

#TODO: Implement the handler factory function that returns different handlers based on the handler_name and handler_properties
def handler_factory(handler_name):
    async def generic_handler(request: Request):
        return {"message": f"Handler {handler_name} processed the request"}
    return generic_handler


def build_routes_from_config():
    sheets_config = get_config()

    for route in sheets_config:
        path = route["route"]
        method = route["method"].upper()
        handler_name = route["handler"]
        handler = handler_factory(handler_name)
        app.add_api_route(path=path, endpoint=handler, methods=[method])


build_routes_from_config()