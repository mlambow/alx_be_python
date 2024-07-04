import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()

    print(current_date.strftime("%Y-%B-%d"))
    print(current_date.strftime("%H:%M:%S"))
display_current_datetime()

def calculate_future_date():
    number_of_days = int(input("Enter a number of days: "))
    date = datetime.datetime.now() + datetime.timedelta(days=number_of_days)
    future_date = date.strftime("%Y-%B-%d")
calculate_future_date()