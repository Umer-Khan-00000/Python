                            # ~~~ CLASSES AND OBJECTS  ~~~

# Making a class named Person --->
class Person :
    Name = "Umer"
    Occupation = "Python Developer"
    NetWorth = 125000

# Creating a method (using self parameter) --->
def info(self):
    print(f"{self.Name} is a {self.Occupation}")

# Calling the method --->
# a = Person()
# a.Name = "Mustafa"
# a.Occupation = "Doctor"
# a.info()

print(f"{Person.Name} is a {Person.Occupation}")
