import time
import datetime


seconds = time.time()
now = datetime.datetime.now()
formatted_date = now.strftime("%b %d %Y")
print(
    f"Seconds since January 1, 1970: {seconds:.4f}"
    f" or {seconds:.2e} in scientific notation"
)
print(formatted_date)
