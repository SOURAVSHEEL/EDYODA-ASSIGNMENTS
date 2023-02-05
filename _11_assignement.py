## Write a Python program to square the elements of a list using map() function.

size = int(input("Enter the size of the list: "))
lst = []
for i in range(size):
    elements = int(input("Enter the elements for the list: "))
    lst.append(elements)
print("The original list is: ",lst)

square = list(map(lambda x: x*x,lst))
print("The square of the original list is: ",square)
