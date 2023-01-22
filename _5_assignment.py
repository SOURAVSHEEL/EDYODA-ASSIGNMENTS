#Write a Python program to print a dictionary whose keys should be 
 #the alphabet from a-z and the value should be corresponding ASCII values



dict = {}

for i in range(97,123):
    dict[chr(i)] = i

print("The dictionary of alphabets to their ASCII values: ")
print(dict)