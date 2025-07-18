
class Animal:
    def __init__(self, name):
        # decalring private variable using __var
        # self.__var_name = var_name
        self.name = name
    # every method we need to create with self parameter
    def speak(self):
            print(f"{self.name} makes sound.")
    # Method overlaoding not possible directly on python
    # def speak(self, name):
    #     print(f"{name}, the {self.name} makes sound ")
    # can be acheived by using default value none
    def describe(self, detail=None):
            if detail == None:
                 print(f"{self.name} is a intelligent one")
            else:
                print(f"{self.name} is a {detail}")
    @staticmethod
    def greet():
        print("Hello!")
    

#Inheritance
class Dog(Animal):
    # Method overloading 
    def speak(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meow.")

# animal object of class Animal
animal = Animal("dog")
dog = Dog("Miles")
cat = Cat("Ken")
#calling speak method
try:
    animal.speak()
    dog.speak()
    cat.speak()
    animal.describe()
    animal.describe("aggressive one")
    print("calling static method")
    Animal.greet()
except Exception as e:
    print(f"exceptiont: {e}")



    