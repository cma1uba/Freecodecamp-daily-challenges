from datetime import datetime

def get_weekday(date_string: str) -> str:
    """
    Given a date string in the format YYYY-MM-DD,
    return the day of the week.

    :param date_string: The date string (e.g., "2025-11-06").
    :return: The day of the week (e.g., "Thursday").
    """
    try:
        # 1. Parse the date string into a datetime object.
        #    The format code '%Y-%m-%d' matches "YYYY-MM-DD".
        date_object = datetime.strptime(date_string, '%Y-%m-%d')

        # 2. Format the datetime object to get the full weekday name.
        #    The format code '%A' gives the full weekday name (e.g., 'Thursday').
        #  Ignore time zones as specified in the challenge.
        weekday_name = date_object.strftime('%A')

      
        # The result from strftime('%A') already follows this format (e.g., "Thursday").
        return weekday_name

    except ValueError:
        # Handle cases where the input string is not a valid date format
        return "Invalid Date Format"

# --- Example Usage ---

# Test for the date in the challenge image: November 6, 2025
challenge_date = "2025-11-06"
print(f"The date {challenge_date} is a: **{get_weekday(challenge_date)}**")

# Test for a different date
test_date_1 = "2023-12-25" # Christmas Day 2023, which was a Monday
print(f"The date {test_date_1} is a: **{get_weekday(test_date_1)}**")

test_date_2 = "2024-01-01" # New Year's Day 2024, which was a Monday
print(f"The date {test_date_2} is a: **{get_weekday(test_date_2)}**")