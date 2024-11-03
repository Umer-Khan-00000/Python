# Cube Function --->
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

NewList = list(map(cube, List))  # Using map function instead of for loop.

# Print all Cubes in a NewList --->
print(NewList)

