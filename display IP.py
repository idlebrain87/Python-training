'''
192.168.0.1
192.168.0.2
192.168.0.3
..
..
192.168.0.10
'''

fixed="192.168.0."
for val in range(1,11):
    ip = fixed +str( val)
    print(ip)
    


l1 = [1,3,5,7,9]
l2 = [2,4,6,8,10]
index = 0
for i in range (1,11,2) :
    l1.insert(i,l2[index])
    index += 1
print(l1)

a,b,c = (1,2,3,4,5,6,7,8,9)[1::3]
print(b)
