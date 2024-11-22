class Person:
    name = "Umer"
    occupation = "Software Developer"
    networth = "120,000"
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        print(f"His net worth is {self.networth} Dollars")

a = Person()
b = Person()
c = Person()

# Changing Name and Occupation --->

# Changing Name on the basis a --->
a.name = "Ali"
a.occupation = "Data Scientest"

# Changing Name on the basis of b --->
b.name = "Hasan"
b.occupation = "Web Devloper"

# Changing Name on the basis c --->
c.name = "Ahmed"
c.occupation = "Photographer"

a.info()
b.info()
c.info()



