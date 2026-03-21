import time

t = time.time()
tl = time.localtime(t)
date_format = time.strftime("%b %d %Y", tl)
print(f"Seconds since January 1, 1970: {t:,.4f} or {t:.2e} in scientific notation")
print(date_format)