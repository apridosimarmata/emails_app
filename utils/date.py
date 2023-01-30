from sqlalchemy import text
from datetime import datetime
import pytz

singapore_tz = pytz.timezone('Asia/Singapore')

def string_to_timestamp(date_str):
    return text(f"to_timestamp('{date_str}', 'DD Mon YYYY HH24:MI')")

def get_now():
    return datetime.now(singapore_tz).replace(second=0).replace(microsecond=0).replace(tzinfo=None)

