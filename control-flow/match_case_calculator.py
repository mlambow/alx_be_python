num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operator (+, -, *, /): ")

match operator:
    case "+":
        sum = num1 + num2
        print("The result is " +str(sum))
    case "-":
        sum = num1 - num2
        print("The result is " +str(sum))
    case "*":
        sum = num1 * num2
        print("The result is " +str(sum))
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else: 
            sum = num1 / num2
            print("The result is " +str(sum))