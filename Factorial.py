def factorial(fact):
    if fact<=0:
        return 1
    else:
        return fact*factorial(fact-1)

print(factorial(5))