#!/usr/bin/env python
# coding: utf-8

# ## Write a program to find all pairs of an integer array whose sum is equal to a given number?

# In[3]:


class Array:
    def __init__(self,size):
        self.size = size
        self.data = []
        self.length = 0
        
    def add(self,data):
        if self.length < self.size:
            self.data.append(data)
            self.length += 1
        else:
            print("Error is size of array is full!")
    
    def findPairs(self,summ):
        print("Pairs whose sum is: ",summ)
        for i in range(len(self.data)):
            for j in range(i,len(self.data)):
                if (self.data[i]+ self.data[j]) == summ:
                    print(self.data[i],self.data[j])
    
    def display(self):
        return self.data

array = Array(8)
array.add(1)
array.add(2)
array.add(3)
array.add(4)
array.add(5)
array.add(6)
array.add(7)
array.add(8)

print(array.findPairs(7))
print(array.display())


# In[ ]:





# ## Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array

# In[4]:


class Array:
    def __init__(self,size):
        self.size = size
        self.data = []
        self.length = 0
        
    def add(self,data):
        if self.length < self.size:
            self.data.append(data)
            self.length += 1
        else:
            print("Error is size of array is full!")
    
    def reverse(self):
        return self.data[::-1]
    
    
    def display(self):
        return self.data

array = Array(8)
array.add(1)
array.add(2)
array.add(3)
array.add(4)
array.add(5)
array.add(6)
array.add(7)
array.add(8)

print(array.display())

print(array.reverse())


# ## Write a program to check if two strings are a rotation of each other?

# In[5]:


def rotation(str1 ,str2):
    if len(str1) != len(str2):
        return False
    
    temp = str1 + str2
    
    if str2 in temp:
        return True
    else:
        return False
    
str1 = input("Enter the string 1:")
str2 = input("Enter the string 2:")

result = rotation(str1,str2)
print(result)


# ## Write a program to print the first non-repeated character from a string?

# In[9]:


def non_repeated(string):
    for i in string:
        if (string.find(i,string.find(i)+1)) == -1:
            print("First non-repeating character is",i)
            break
string = input("Enter the string: ")
result = non_repeated(string)
print(result)


# ## Read about the Tower of Hanoi algorithm. Write a program to implement it.

# In[10]:


def TowerOfHanoi(n,from_rod,to_rod,aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1,from_rod,aux_rod,to_rod)
    print (f"Move disk {n} from rod {from_rod} to rod {to_rod}")
    TowerOfHanoi(n-1,aux_rod,to_rod,from_rod)

TowerOfHanoi(3,"A","C","B")


# ## Write a program to convert prefix expression to infix expression

# In[13]:


def prefix_to_infix(prefix):
    stack = []
    operators = set(["+","-","/","*","^"])
    prefix = prefix[::-1]
    for i in prefix:
        if i in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append('({} {} {})'.format(op1,i,op2))
        else:
            stack.append(i)
    return stack.pop()

prefix = '*+AB-CD'
infix = prefix_to_infix(prefix)
print(infix)
    


# ## Write a program to check if all the brackets are closed in a given code snippet

# In[18]:


def brackets(code):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"
    for i in code:
        if i in opening_brackets:
            stack.append(i)
        elif i in closing_brackets:
            if not stack:
                return False
            top = stack.pop()
            if opening_brackets.index(top) != closing_brackets.index(i):
                return False
    return not stack

code = "{[(5+9)*3]/(16-7)}"
if brackets(code):
    print("All brackets are properly closed")
else:
    print("Umatched brackets found")


# ## Write a program to reverse a stack.

# In[19]:


class Stack:
    
    def __init__(self):
        self.data = []
        
    def isEmpty(self):
        return len(self.data) == 0
    
    def push(self,data):
        self.data.append(data)
        
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        return self.data.pop()
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        return self.data[-1]
    
    def size(self):
        return len(self.data)
    
def insertAtBottom(stack,data):
    if stack.isEmpty():
        stack.push(data)
    else:
        temp = stack.pop()
        insertAtBottom(stack,data)
        stack.push(temp)

def reverseStack(stack):
    if not stack.isEmpty():
        temp = stack.pop()
        reverseStack(stack)
        insertAtBottom(stack,temp)
        
stack = Stack()
stack.push(2)
stack.push(4)
stack.push(8)
stack.push(11)

print("Original stack:")
print(stack.data)

reverseStack(stack)


print("Reversed stack:")
print(stack.data)


# ## Write a program to find the smallest number using a stack

# In[20]:


class Stack:
    
    def __init__(self):
        self.data = []
        
    def isEmpty(self):
        return len(self.data) == 0
    
    def push(self,data):
        self.data.append(data)
        
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.data.pop()
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.data[-1]
    
    def size(self):
        return len(self.data)
    
    def view(self):
        return self.data

def smallest_number(stack):
    if stack.isEmpty():
        print("Stack is empty")
    
    smallest = stack.pop()
    while not stack.isEmpty():
        data = stack.pop()
        if data < smallest:
            smallest = data
    return smallest

stack = Stack()
stack.push(2)
stack.push(4)
stack.push(8)
stack.push(11)
stack.push(5)
stack.push(3)
stack.push(7)
print(stack.view())
print(smallest_number(stack))


# In[ ]:





# In[ ]:




