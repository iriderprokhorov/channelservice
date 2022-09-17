from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from pycbrf import ExchangeRates
from datetime import datetime
import psycopg2
import os
import requests


from dotenv import load_dotenv

load_dotenv()


SERVICE_ACCOUNT_FILE = "service_google.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

SAMPLE_SPREADSHEET_ID = os.getenv("SHEET_ID")
SAMPLE_RANGE_NAME = "A1:D100"


def send_message(text):
    token = os.getenv("TOKEN")
    chat_id = os.getenv("CHAT_ID")
    url_req = (
        "https://api.telegram.org/bot"
        + token
        + "/sendMessage"
        + "?chat_id="
        + chat_id
        + "&text="
        + text
    )
    results = requests.get(url_req)
    print(results.json())


def get_currency():
    try:
        rates = ExchangeRates()
        usd_rate = rates["USD"].value
    except Exception:
        print("i can't get currency")
    return usd_rate


def main():
    """Shows basic usage of the Sheets API.
    Delete 1 row from a spreadsheet.
    """
    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(
                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range=SAMPLE_RANGE_NAME,
            )
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

    except HttpError as err:
        print(err)
    # delete first row
    values.pop(0)

    return values


if __name__ == "__main__":
    sheet_values = main()
    usd_currency = get_currency()
    today = datetime.now().date()

# establishing the connection to db
try:
    conn = psycopg2.connect(
        database=os.getenv("DB_NAME"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )
    cursor = conn.cursor()
    cursor.execute("DELETE from orders_order")
    for each in sheet_values:
        if datetime.strptime(each[3], "%d.%m.%Y").date() < today:
            send_message(each)
        each.append(round(int(each[2]) * usd_currency, 2))
        cursor.execute(
            "INSERT into orders_order(number, order_number, price_usd, srok_postavki, price_rub) VALUES (%s, %s, %s, %s, %s)",
            each,
        )
    conn.commit()
except (Exception, psycopg2.Error) as error:
    print("Failed to insert records into table", error)
finally:
    conn.close()
    print("Datasheets are inserted successfully")
