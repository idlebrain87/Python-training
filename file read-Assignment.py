
# fobj can be called as file object or file handler or pointer
'''
with open('realestate.csv','r') as fobj:
    for line in fobj:
        # remove any white spaces and line breaks
        line =line.strip()
        print(line)



# displaying street and city

with open('realestate.csv','r') as fobj:
    for line in fobj:
        # remove any white spaces and line breaks
        line =line.strip()
        output = line.split(",")
        print ("street :", output[0])
        print ("street :", output[1])
        print ("----------------------")



# displaying street and city

with open('realestate.csv','r') as fobj:
    for line in fobj:
        # remove any white spaces and line breaks
        line =line.strip()
        output = line.split(",")
        print (output[0].ljust(20), "\t", output[1])


      
# displaying only unique city and count 

cityset  = set()
with open('realestate.csv','r') as fobj:
    # processing 
    for line in fobj:
        # remove any white spaces and line breaks
        line =line.strip()
        output = line.split(",")
        city = output[1]
        cityset.add(city)
    # display the output
    for city in cityset:
        print(city)
    print("total no of cities :", len(cityset))


# Write a Python program to read realestate.csv and
#display all the UNIQUE cities and the count of unique citiesand number of times each city is repeated 



citylist  = list()

## display only street and city
with open('realestate.csv','r') as fobj:
    # processing 
    for line in fobj:
        # remove any white spaces and line breaks
        line =line.strip()
        output = line.split(",")
        city = output[1]
        citylist.append(city)
    # display the output
    for city in set(citylist):
        print(city.ljust(20), citylist.count(city),'times') 
    print("No. of cities :", len(set(citylist)))

'''


# using readline()
'''
with open('data.txt','r') as fobj:
    print(fobj.readline())
    print(fobj.readline())
    print(fobj.readline())
    print(fobj.readline())
    print(fobj.readline())


with open('data.txt','r') as fobj:
    for line in fobj:
        while True:
            line = fobj.readline()
            if not line:
                break
            print(line)



try:    
    filename = input("Enter any filename :")
    with open(filename,'r') as fobj:
        for line in fobj:
            print(line)
except Exception as error:
    print("user defined error:","file doesn't exist")
    print(error)

print('regular code')
'''

try:
    #1st logic
    filename = input("Enter any filename :")
    with open(filename,'r') as fobj:
        for line in fobj:
            print(line)
    #2nd logic
    val = str(3) + "hello"

except FileNotFoundError as error:
    print("File doen't exist.. pl check")
    print(error)
except TypeError as error:
    print("Invalid operation")
    print(error)
except ValueError as err:
    print("Invalid conversion")
    print(error)
except (IndexError, KeyError ) as err:
    print("key or index is not existing.. pl check")
except Exception as err:
    print("System error :" , err)
else:
    print("few lines of code")
