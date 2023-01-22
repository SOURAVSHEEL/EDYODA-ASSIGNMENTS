#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples



#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


tup = [(2,5),(1,2),(4,4),(2,3),(2,1)]
lst1 = len(tup)
for i in range(0,lst1):
    for j in range(0,lst1-i-1):
        if(tup[j][-1]>tup[j+1][-1]):
            temp = tup[j]
            tup[j] = tup[j +1]
            tup[j +1] = temp
print(tup)


