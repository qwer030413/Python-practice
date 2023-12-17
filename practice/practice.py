class davib:
    name = ""
    age = None
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        
        

a = 1
a = "asdasd"

c = input("What is your name:")
d = input("what is your age:")
obj = davib(c,d)

print(obj.name + " " + obj.age) 

