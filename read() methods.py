
#Example commented out for appendding in a file :

# f = open('Day 50 Example.txt', 'r')
# text = f.read()
# print(text)
# f.close()

# with open('Day 50 Example.txt', 'a') as f:
#   f.write("Hello Everyone\n")


f = open('Day 50 Example.txt', 'r')
while True:
  line = f.readline()
  print(line)
  if not line:
    break
