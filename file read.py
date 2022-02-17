
# fobj can be called as file object or file handler or pointer
with open('data.txt','r') as fobj:
    for line in fobj:
        # remove any white spaces and line breaks
        line =line.strip()
        print(line)

print("---------------")
#just display the line containing python
#fobj can be called as file object or file handler or pointer
with open ('data.txt','r') as fobj:
    for line in fobj:
        #remove any white spaces 
        line =line.strip()
        if 'python'.lower() in line.lower():
            print(line)
            
