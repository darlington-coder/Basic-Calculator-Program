number1 = float(input("Enter First Number "))
number2 = float(input("Enter Second Number "))
operator = input("Enter Any of these Mathematical operators(+, -, *, /) ")

if operator == "+":
    sum = number1 + number2
    print(number1, "+ ", number2, "= ", sum)
elif operator == "-":
    difference = number1 - number2
    print(number1, "- ", number2, "= ", difference)
elif operator == "*":
    product = number1 * number2
    print(number1, "* ", number2, "= ", product)
elif operator == "/":
    quotient = number1 / number2
    print(number1, "/ ", number2, "= ", quotient)
else:
    print("incorrect!,Enter Any of The Above Mentioned Operators")



