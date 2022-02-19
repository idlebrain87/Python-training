
# to reverse a user input string 


def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
  
s = input("enter the name to be reversed :")
  
print ("The input string  is : ",s)
  
print ("The reversed string is : ",reverse(s))
