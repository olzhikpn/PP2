class StringHandler:
    def init(self):
        self.s = ""
    
    def getString(self):
        self.s = input("Enter a string: ")
    
    def printString(self):
        print(self.s.upper())