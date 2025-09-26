
def printList(lst, index):
    if(index >= len(lst)):
        return
    print(lst[index], end=" ")
    printList(lst, index+1)

    
lst = [1,2,3,4,5,6,7,8,9,10]
printList(lst, 0)