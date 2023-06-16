def add_time(start, duration, start_day=None):

    #Replacing the ":" with " " so I only have to use split once.
    #Time split into seperate variables by hour, minute, and AM/PM
    start = start.replace(":", " ")
    start_parts = start.split(" ")

    start_hour = int(start_parts[0])
    start_minute = int(start_parts[1])
    AM_or_PM = start_parts[2]

    # Same done for duration except replace function is not needed

    duration_parts = duration.split(":")

    duration_hours = int(duration_parts[0])
    duration_minutes = int(duration_parts[1])

    #Converts start time hour to 24 hour clock time if start time is PM. Converts by adding 12 to the PM hour.

    if AM_or_PM == "PM":
        start_hour = 12 + start_hour

    # Defining multiple variables, including variables for determining max minutes in an hour and max hours in a day.
    current_minute = start_minute
    current_hour = start_hour
    days_passed = 0
    max_minute = 60
    max_hour = 24

    # Using for loops to add the duration time and increases the hour by one if the minute time reaches 60, and brings minute time back to 0. If the hour reaches 24, days_passed is increased by 1 and the hour is set to 0.

    for minute in range(duration_minutes):
        current_minute += 1
        if current_minute >= max_minute:
            current_hour += 1
            current_minute = 0

    for hour in range(duration_hours):
        current_hour += 1

        if current_hour >= max_hour:
            days_passed += 1
            # If the boolean is placed at the start of the loop, on the last iteration the hour could be 23, and be raised to 24, and the boolean wouldn't
            # add one more to days passed and set the hour to 0.
            # The current_hour - max_hour is used in the very specific case of when in the increasing minute time loop, the hour is raised from 23 to 24,
            # and at the start of this loop the current hour is raised further from 24 to 25, then current_hour - max_hour will set the current_hour to 1.
            current_hour = current_hour - max_hour

    # Converts the hour and minute into a string, and adds a 0 before the minute if it is 1 digit. Example: 7th minute of 12 o clock is 12:07.
    # Also converts the 24 hour clock time back to the 12 hour clock and determines whether time is AM or PM.
    current_minute = str(current_minute)
    if len(current_minute) == 1:
        current_minute = "0" + current_minute

    #  0:00 in 24 clock time is 12:00 AM, so 0 is changed into 12
    if current_hour < 12:
        if current_hour == 0:
            current_hour = "12"
        else:
            current_hour = str(current_hour)

        AM_or_PM = "AM"

    elif current_hour >= 12:
        if current_hour == 12:
            current_hour = "12"
        else:
            current_hour = str(current_hour - 12)

        AM_or_PM = "PM"

    time_now = f"{current_hour}:{current_minute} {AM_or_PM}"

    if days_passed == 0:
        days_passed_msg = ""

    elif days_passed == 1:
        days_passed_msg = " (next day)"

    elif days_passed > 1:
        days_passed_msg = f" ({days_passed} days later)"

    # If the function is provided the starting day of the week, the code below will be used to determine what day of week it is after the time passed.

    if start_day != None:
        start_day = start_day.lower()

        # First day considered as the zeroeth day
        days_of_week = [
            "monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
            "sunday"
        ]
        if start_day in days_of_week:
            nth_day_of_week = days_of_week.index(start_day)

            max_nth_day = 7
            for day in range(days_passed):
                nth_day_of_week += 1
                if nth_day_of_week == max_nth_day:
                    nth_day_of_week = 0

            the_day = days_of_week[nth_day_of_week].title()

        return f"{current_hour}:{current_minute} {AM_or_PM}, {the_day}{days_passed_msg}"

    else:
        return f"{current_hour}:{current_minute} {AM_or_PM}{days_passed_msg}"
