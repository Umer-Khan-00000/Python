
            # ******^^^****** :: LAMBDA FUNCTIONS :: ******^^^******

# Making functions --->
double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x,y: (x + y)/2

# Print the functions --->
print(double(5))
print(cube(5))
print(avg(5, 5))

# Passing a fuction inside a function --->
def appl(fx, value):
    return 6 + fx(value)

# Printing this function --->
# print(appl(lambda x : x * x, 2)) ---> Use This 
print(appl(cube, 2)) # <--- Or This

