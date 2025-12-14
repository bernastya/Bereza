class User:
    age = 0


    def __init__(self, name):
        print("я создался")
        self.username = name


    def sayname(self): 
         print("Меня зовут", self.username)   


    def sayage(self):
        print(self.age)
    

    def satage(self, newage):
        self.age = newage