from sqlalchemy import text
from datetime import datetime

def string_to_timestamp(date_str):
    return text(f"to_timestamp('{date_str}', 'DD Mon YYYY HH24:MI')")

def get_now():
    return datetime.now()

