import json


class Employee:

    def __init__(self,Name,DOB,Height,City,State):
        self.Name = Name
        self.DOB = DOB
        self.Height = Height
        self.City = City
        self.State = State

with open('C:\\Users\\soura\\OneDrive\Desktop\\DATA SCIENCE\\EDYODA ASSIGNMENTS\\Json_assignemt\\employee.json') as file:
    data = json.load(file)

employees = []

for emp in data['employees']:
    employees.append(Employee(emp['Name'],emp['DOB'],emp['Height'],emp['City'],emp['State']))

for emp in employees:
    print(emp.__dict__)