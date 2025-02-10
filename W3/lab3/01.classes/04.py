class Point:
    def init(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        return ((self.x - other_point.x)  2 + (self.y - other_point.y)  2) ** 0.5