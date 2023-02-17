## SQUARE NUMBERS AND RETURN THEIR SUM

class Point:

    def __init__(self):
        self.x =int(input("Enter value for x: "))
        self.y = int(input("Enter value for y: "))
        self.z = int(input("Enter value for z: "))

    def sqSum(self):
        return self.x**2 + self.y**2 + self.z**2
    
point = Point()
print(point.sqSum())