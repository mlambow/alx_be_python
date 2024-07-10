def safe_divide(numerator, denominator):
    try:
        num = numerator
        deno = denominator
        num / deno
    except ZeroDivisionError:
        print("You can not divide by zero")
    except ValueError:
        print("Please insert a number")
    else:
        print()