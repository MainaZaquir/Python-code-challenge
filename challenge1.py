def convert_to_24_hour_format(hour, minute, period):
    # Adjusting the hour based on the period
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0

    # Formatting the result as a four-digit string
    result = "{:02d}{:02d}".format(hour, minute)
    
    return result

# Examples
print(convert_to_24_hour_format(10, 50, "am"))  # The output: 1050
print(convert_to_24_hour_format(10, 50, "pm"))  # The output: 2250
print(convert_to_24_hour_format(12, 45, "am")) # The output: 0045
print(convert_to_24_hour_format(12, 15, "pm")) # The output: 1215
print(convert_to_24_hour_format(1, 20, "am")) # The output: 0120
print(convert_to_24_hour_format(1, 20, "pm")) # The output: 1320
