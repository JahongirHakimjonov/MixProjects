numberOne = float(input("1-son->"))
numberTwo = float(input("2-son->"))
calculation = input("Amalni kiriting->(+, -, *, /)")
if calculation == "+":
    result = numberOne + numberTwo
    print("Natija=", result)
elif calculation == "-":
    result = numberOne - numberTwo
    print("Natija=", result)
elif calculation == "*":
    result = numberOne * numberTwo
    print("Natija=", result)
elif calculation == "/":
    result = numberOne / numberTwo
    print("Natija=", result)
else:
    print("Notogri amal kiritildi")
