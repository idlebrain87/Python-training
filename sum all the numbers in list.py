#Python code to sum all the numbers in a list

alist = [8, 2, 3, 0, 7]
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

print ("given list =", alist)
print('sum of given list = ',alist[0],'+',alist[1],'+' ,alist[2],'+',alist[3],'+',alist[4],'=',sum(alist))
