# creating a class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
# creating method introduce
def introduce (self):
    print(f"hello, my name is {self.name}, i am {self.age} years old, and i am {self.gender}")
    
# creating an instance metod to the person class

person1 = Person("Linda", 150, "Female")
         
# invoking the introduce method to display the person information

person1.introduce()