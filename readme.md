
# Dynamic FastAPI Routes from Google Sheets

This project dynamically builds FastAPI routes based on configurations stored in a Google Sheets document. Each route, HTTP method, and handler is defined in the sheet, allowing you to update your API routes without changing the code.

## Project Structure

dyn_fastapi_sheets
├── api.py                         # Main FastAPI app, loads routes dynamically from Google Sheets
├── sheets_adapter.py              # Adapter for Google Sheets API to fetch configuration data
├── models.py                      # (Placeholder for data models if needed)
├── main.py                        # Entry point to run the FastAPI app
└── .env                           # Environment variables for credentials and sheet details
└── env                            # Folder containing the google sheets auth file

## Setup

### Prerequisites

	•	Python 3.12 or higher
	•	Google Cloud service account
	•	FastAPI
	•	gspread

### Installation

	1.	Clone the repository:

`git clone https://github.com/your-username/dyn_fastapi_sheets.git`
`cd dyn_fastapi_sheets`


	2.	Install dependencies:

`pip install -r requirements.txt`


	3.	Set up your .env file:
Create a .env file in the project root with the following values:

CREDENTIAL_FILE=path_to_your_credentials.json
SHEET_ID=your_google_sheet_id
SHEET_NAME=Sheet1


	4.	Add your Google Sheets service account credentials to the project root, e.g., playground-438509-58046b106ea8.json.

Running the Application

	1.	Start the FastAPI application:

uvicorn main:app --reload


	2.	Access the API at http://localhost:8000.

How it Works

	1.	The sheets_adapter.py fetches data from a Google Sheet containing the API configuration (route, method, handler).
	2.	api.py dynamically builds API routes based on the sheet data, with each handler linked to a specific route and HTTP method.
	3.	You can extend handler_factory to implement different handler logic based on the sheet configuration.

Google Sheets Configuration

Your Google Sheet should have the following headers in the first row:

route	method	body	handler
/foo	GET	None	my_handler

	•	route: Path for the API route (e.g., /foo)
	•	method: HTTP method (e.g., GET, POST)
	•	body: (Optional) Expected body content
	•	handler: Name of the handler function

Future Enhancements

	•	Implement more dynamic handler logic in handler_factory.
	•	Add validation for the request body based on the configuration.
	•	Implement authentication and authorization.

