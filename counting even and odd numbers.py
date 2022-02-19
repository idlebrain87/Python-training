
# list as per teh Assessment 
alist = [1,2,3,4,5,6,7,8,9]


evenlist = []
oddlist = []
for val in alist:
    if val % 2 ==0 :
        evenlist.append(val)
    else:
        oddlist.append(val)

print ("the given numbers are", alist)
print ("No. of even numbers:", len(evenlist))
print ("No. of even numbers:", len(oddlist))

