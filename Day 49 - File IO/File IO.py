
# Reading the file :

f = open('Day 49 Example.txt', 'r')
text = f.read()
print(text)
f.close()

# Writing to a file :

f = open('Day 49 Example.txt', 'a')
f.write("This is a new line added by me.\n")
f.close()

with open('Day 49 Example.txt', 'a') as f:
  f.write("This is a new line added by me")

 