# writing to file
#if the file is not exiting, it will create or else overwrites
'''
fobj = open("customers.txt","w")
fobj.write('python programming\n')
fobj.write('scala programming\n')
fobj.close()

#writing numbers to the file
#if the file is not exiting, it will create or else it will append
fobj = open("customers1.txt","a")
for line in range(1,10):
    fobj.write(str(line) + "\n")
fobj.close()

#modern style- pythonic way
#context manager
#advantage file will be closed automatically

with open("modernstyle.txt",'w') as fobj:
    fobj.write('python programming\n')
    fobj.write('java\n')

'''
    
## Replace SACRAMENTO with BANGALORE
with open('realestate.csv','r') as fobj:
    # processing 
    for line in fobj:
        # remove any white spaces and line breaks
        line =line.strip()
        if 'SACRAMENTO' in line :
            line=line.replace('SACRAMENTO','BANGALORE')
        
        print(line) 

