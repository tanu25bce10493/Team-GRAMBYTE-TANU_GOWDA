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

def log_booking(booking_data: dict) -> None:
    """
    Save one booking into the journal file.
    """