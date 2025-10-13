def to_12(time):
    """
    Converts a time string from "HHMM" (24-hour) format to "H:MM AM/PM" (12-hour) format.

    Args:
        time (str): A four-digit string representing time in 24-hour format (e.g., "1305").

    Returns:
        str: The time in 12-hour format (e.g., "1:05 PM").
    """
    # 1. Extract hours (HH) and minutes (MM)
    hours_24_str = time[:2]
    minutes_str = time[2:]

    # Convert 24-hour string to integer
    hours_24 = int(hours_24_str)

    # 2. Determine AM/PM suffix
    if 0 <= hours_24 < 12:
        suffix = "AM"
    else:  # 12 <= hours_24 <= 23
        suffix = "PM"

    # 3. Convert 24-hour to 12-hour time
    if hours_24 == 0:
        # Midnight (0000 to 0059) becomes 12:XX AM
        hours_12 = 12
    elif hours_24 == 12:
        # Noon (1200 to 1259) becomes 12:XX PM
        hours_12 = 12
    else:
        hours_12 = hours_24 % 12
    return f"{hours_12}:{minutes_str} {suffix}"

# --- Examples ---
print(f"'0000' -> {to_12('0000')}")    # Expected: "12:00 AM" (Midnight)
print(f"'0130' -> {to_12('0130')}")    # Expected: "1:30 AM"
print(f"'1159' -> {to_12('1159')}")    # Expected: "11:59 AM"
print(f"'1200' -> {to_12('1200')}")    # Expected: "12:00 PM" (Noon)
print(f"'1305' -> {to_12('1305')}")    # Expected: "1:05 PM"
print(f"'2359' -> {to_12('2359')}")    # Expected: "11:59 PM"
print(f"'1545' -> {to_12('1545')}")    # Expected: "3:45 PM"
print(f"'0910' -> {to_12('0910')}")    # Expected: "9:10 AM"