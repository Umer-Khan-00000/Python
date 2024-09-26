# You can either use this program

# marks = [68, 79, 55, 98, 93, 91]

# index = 0
# for mark in marks:
#     print(mark)
#     if (index == 3):
#         print("Umer got 98 Marks")
#     index +=1

#--------- OR ---------

# Use the one with enumerate function :

marks = [68, 79, 55, 98, 93, 91]

for index, mark in enumerate(marks):    # enumerate function shorten the code.
    print(mark)
    if (index == 3):
        print("Umer got 98 Marks")
