x = 10

def my_function():
  global x
  x = 5 # Changes to global variable x
  y = 5 # Local variable

my_function()
print(x)

