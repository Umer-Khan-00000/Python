

                                        # READ-LINES() METHODS :
# -------------------------------------------------------------------------------------------------------- #


#Example commented out for appendding in a file :

# f = open('Day 50 Example.txt', 'r')
# text = f.read()
# print(text)
# f.close()

# with open('Day 50 Example.txt', 'a') as f:
#   f.write("Hello Everyone\n")

                                      # THE END OF THE 1ST EXAMPLE #
# --------------------------------------------------------------------------------------------------------- #


# f = open('Day 50 Example.txt', 'r')
# while True:
#   line = f.readline()
#   print(line)
#   if not line:
#     break

                                      # THE END OF THE 1ST PROGRAM #
# --------------------------------------------------------------------------------------------------------- #

  # A use-case for student marks :

# f = open('Day 50 Example.txt', 'r')
# i = 0
# while True:
#   i = i + 1
#   line = f.readline()
#   if not line:
#     break
#   m1 = line.split(",")[0]
#   m2 = line.split(",")[1]
#   m3 = line.split(",")[2]

#   print(f"\nThe Marks of student {i} in Mathematics are {m1}\n")
#   print(f"The Marks of student {i} in English are {m2}\n")
#   print(f"The Marks of student {i} in Geography are {m3}\n")

#   # WILL FIGURE THE PERCENTAGE SECTION LATER :
  
#   totalMarks = 300
#   ObtMarks = m1 
#   Percentage = totalMarks / ObtMarks * 100

#   print(f"\nThe Percentage of student {i} is {Percentage}\n")
#   print(f"The Percentage of student {i} is {Percentage}\n")
#   print(f"The Percentage of student {i} is {Percentage}\n")


                                    # THE END OF THE USE-CASE EXAMPLE #
# --------------------------------------------------------------------------------------------------------- #

                                        
                                        # WRITE-LINES() METHODS :
# --------------------------------------------------------------------------------------------------------- #

f = open("Day 50 Example2.txt", "w")
lines = ["line1\n", "line2\n", "line3\n"]
f.writelines(lines)
f.close()

