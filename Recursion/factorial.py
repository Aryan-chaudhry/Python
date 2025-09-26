
def getFactorial(n):
    # base case
    if(n == 0):
        return 1
    
    return n*getFactorial(n-1)

number = 5;
factorial = getFactorial(number)
print(factorial)