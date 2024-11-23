                        # ~~~ Constructors in Pythob ~~~

# Example for assinging variables and Printing from a Function --->

class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age
   
        

    def info(self):
        print("\nExample for assinging variables and Printing from a Method ---> ")
        print(f"My name is {self.name} and my age is {self.age}")    

a = Person("Umer", 15)
a.info()