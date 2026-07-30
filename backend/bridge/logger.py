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