import json
import os
from datetime import datetime

DATABASE_FOLDER = os.path.join(
    os.path.dirname(__file__),
    "..",
    "database"
)

JOURNAL_FILE = os.path.join(
    DATABASE_FOLDER,
    "journal.json"
)


def load_bookings():

    os.makedirs(DATABASE_FOLDER, exist_ok=True)

    if not os.path.exists(JOURNAL_FILE):
        with open(JOURNAL_FILE, "w") as f:
            json.dump([], f)

    with open(JOURNAL_FILE, "r", encoding="utf-8") as f:

        try:
            return json.load(f)
        except:
            return []


def log_booking(booking_data):

    bookings = load_bookings()

    booking_data["timestamp"] = datetime.now().isoformat()

    bookings.append(booking_data)

    with open(JOURNAL_FILE, "w", encoding="utf-8") as f:

        json.dump(bookings, f, indent=4)