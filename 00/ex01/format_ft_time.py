

from datetime import datetime
import time
today = datetime.now()
year = today.strftime("%Y")
month = today.strftime("%b")
day = today.strftime("%d")
today_date = today.strftime("%Y %b %d")



leap_seconds = time.time()
ref = datetime(1970, 1, 1)
scientific_format = "{:e}".format(leap_seconds)
print(f"Seconds since January 1, 1970: {leap_seconds} or {scientific_format} in scientific notation")
print(today_date)
