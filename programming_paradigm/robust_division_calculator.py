def safe_divide(numerator, denominator):
    try:
        #convert inputs to floats
        num = float(numerator)
        deno = float(denominator)

        #division and zero division handle
        try:
            result = num / deno
            return f"The result of the division is {result:.2f}"
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")