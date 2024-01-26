# Assignment 5:
# Do the exercise 1-15 in https://pynative.com/python-basic-exercise-for-beginners/
# Try do challenge yourself by not checking the "solution"

# Exercise 8:
# Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# use a loop and range
rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print()