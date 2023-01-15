# Write a Python program to get the Fibonacci series between 0 to 50

nterm = int(input ("Enter the terms you wants to print? "))  

num1 = 0  
num2 = 1  
count = 0  
  
if nterm <= 0:  
    print ("Please enter a positive integer and non-zero interger")  

elif nterm == 1:  
    print ("The Fibonacci sequence of the numbers up to", nterm, ": ")  
    print(num1)  
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < nterm:  
        print(num1)  
        nth = num1 + num2    
        num1 = num2  
        num2 = nth  
        count += 1  