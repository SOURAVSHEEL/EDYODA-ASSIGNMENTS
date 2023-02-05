# Write a Python program to create a lambda function 
# that adds 25 to a given number passed in as an argument.


num = int(input("Enter the number: "))

add = lambda x  : x + 25
print(add(num))