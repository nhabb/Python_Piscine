import time
import datetime
seconds = time.time()
formated = format(seconds,",.4f")
scientific = format(seconds,".2e")
print(f"Seconds since January 1, 1970: {formated} {scientific} in scientific notation")
print(datetime.datetime.now().strftime("%b %d %Y"))