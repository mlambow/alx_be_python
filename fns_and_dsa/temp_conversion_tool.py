FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5



def convert_to_celsuis(fahrenheit):
    celsuis = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsuis

def convert_to_fehrenheit(celsuis):
    fahrenheit = (celsuis * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        weather = input("Is this temperature in Celsuis or Fahrenheit? (C/F): ")

        if weather == 'C':
            converted_temperature = convert_to_fehrenheit(temperature)
            print(f"{temperature}F is {converted_temperature}C")
        elif weather == 'F':
            converted_temperature = convert_to_celsuis(temperature)
            print(f"{temperature}C is {converted_temperature}F")
        else:
            print("Invalid weather unit. Please enter 'C' for Celsuis or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

