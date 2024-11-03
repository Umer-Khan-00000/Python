                    # ^^^^^***^^^^^ MAP Methods / Functions ^^^^^***^^^^^

# Function to cube a number --->
def cube(x):
    return x*x*x

# print(cube(2))

# Example of getting cubes of all nums --->
# Very Long Function Step --->
# This is not a very efficient way of writing code --->

List = [1, 2, 3, 4, 5, 6, 7, 8]
NewList = []

for items in List:
        NewList.append(cube(items))

# Short Function Step (using map) --->
# So Use this instead of using long for loops --->

print("\nThis is an output for map() function :")
NewList = list(map(cube, List))  # Using map function instead of for loop.

# Print all Cubes in a NewList --->
print(NewList)

                # ^^^^^***^^^^^ FILTER Methods / Functions ^^^^^***^^^^^

# Function to filter --->
def filter_func(a):
      return a>2

print("\nThis is an output for Filter Function :")
List2 = list(filter(filter_func, List))
print(List2)                


                # ^^^^^***^^^^^ REDUCE Methods / Functions ^^^^^***^^^^^   

from functools import reduce
# List of numbers --->
List3 = [1, 2, 3, 4, 5]

# Calculating Sum of all Numbers --->
def sum(x, y):
      return x + y

sum = reduce(sum, List3)

# Printing Sum of all Numbers --->
print("\nThis is an output for reduce method :")
print(sum)
 