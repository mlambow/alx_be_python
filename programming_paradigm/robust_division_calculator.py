def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        deno = float(denominator)
        num / deno
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Please enter numeric values only")
    else:
        print()