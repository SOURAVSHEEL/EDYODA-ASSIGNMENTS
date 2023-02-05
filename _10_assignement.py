#Write a Python program to triple all numbers of a given list of integers. Use Python map.


size = int(input("Enter the size of the list: "))
lst = []
for i in range(size):
    elements = int(input("Enter the element of the list: "))
    lst.append(elements)
print("Original list: ", lst)

result = list(map(lambda x: x + x + x, lst)) 
print("Triple of original list numbers: ",result)
