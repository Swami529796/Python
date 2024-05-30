income = int(input())
if income <= 10000:
    print(income)
elif income > 10000 and income <= 20000:
    mul = income * 0.1
    print(mul)
else:
    print(income *0.2)