# # Default Arguments (Example Of Average) :

a = 3
b = 9

def average(a, b, c = 1):
  print("The average is ", (a + b + c) / 2)

# # Arbitary Arguments :

def name(*name):
  print("Hello,", name[0], name[1], name[2])

name ("James", "Barnes", "Buchanan ")  

# # Keyword Arbitary Arguments (Example Of Name) :

def name(**name):
  # print(type(name))
  print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname="Shahid", lname="Ali", fname="Umer")

# Another Average Example :
def average(*numbers):
  # print(type(numbers))
  sum = 0 
  for i in numbers :
    sum = sum + i
  # print("Average is:", sum / len(numbers))
  
  # the 1st value will return instead of the 2nd statement :
  return sum / len(numbers)



c = average(4, 9, 4, 7)
print(c)    

# Example Of Greet Message :

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Call with both arguments
greet("Alice", "Hi")  # Output: Hi, Alice!

# Call with default greeting
greet("Bob")  # Output: Hello, Bob!

print("Alice, Hi")

# Real-Life Examples :
    # Example 01 :
def make_pizza(pizza_type, toppings):
    # Code to make pizza
    print("Making a " + pizza_type + " pizza with " + toppings + " toppings!")

# Calling the function
make_pizza("Fajita", "Pepperonni")

    # Example 02 :

def greet(name, greeting="Hello"):
    print(greeting + ", " + name)

greet("Bob")
greet("Bob", "Hi")


def greeting(name, age, gender="male"):
    print("Hello, %s. You are %d years old and you are a %s."
     % (name, age, gender))

greeting("Bob", 25)


# End of File : Day - 21.py

