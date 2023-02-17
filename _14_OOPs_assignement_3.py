## IMPLEMENT THE COMPLETE STUDENT CLASS

class Student:

    def __init__(self,__name,__rollNumber):
        self.__name = __name
        self.__rollNumber = __rollNumber

    def setName(self,__name):
        self.__name = __name

    def getName(self):
        return self.__name
    
    def setRollNumber(self,__rollNumber):
        self.__rollNumber = __rollNumber

    def getRollNumber(self):
        return self.__rollNumber
    
student = Student("Sourav",21)

print(student.getName())
print(student.getRollNumber())