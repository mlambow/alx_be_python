def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        deno = float(denominator)
        num / deno
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only")
    else:
        print()