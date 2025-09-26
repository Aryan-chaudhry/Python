def getSum(no, end):
    if(no > end):
        return 0
    return no + getSum(no+1, end)
    

no = 1
totalSum = getSum(no, 5)
print(totalSum)