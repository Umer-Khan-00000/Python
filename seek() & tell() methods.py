
# -------------------------------SEEK() & TELL() METHODS--------------------------

# -------------------------------EXAMPLE NO. 01 :--------------------------


# with open('Day 51 Example.txt', 'r') as f:
#     print(type(f))
#     # Moves the cursor after 10th bytes in the file
#     f.seek(10)

#     # Read the next 5 bytes :
#     data = f.read(5)
    # print(data)


# -------------------------------EXAMPLE NO. 02 :--------------------------

with open('Day 51 Example2.txt', 'w') as f:
    f.write("Hello World3 !")
    f.truncate(3)

with open('Day 51 Example2.txt', 'r') as f:
    print(f.read())    




