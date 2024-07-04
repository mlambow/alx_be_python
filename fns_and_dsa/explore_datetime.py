from datetime import datetime, timedelta, date

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%B-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(number_of_days ):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days )
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    display_current_datetime()

    try:
        number_of_days  = int(input("Enter a number of days: "))
        calculate_future_date(number_of_days )
    except ValueError:
        print("Invalid input. Please enter an interger ")

if __name__ == "__main__":
    main()