from turtle import Shape

class Rectangle(Shape):
    def init(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width