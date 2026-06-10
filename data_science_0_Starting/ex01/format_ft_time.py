import time

current_time = time.time()
formatted_current_time = format(current_time, ",.4f")
scientific_notation = format(current_time, ".2e")

date = time.strftime("%b %d %Y")

print(
    f"Seconds since January 1, 1970: {formatted_current_time} "
    f"or {scientific_notation} in scientific notation"
)
print(date)
