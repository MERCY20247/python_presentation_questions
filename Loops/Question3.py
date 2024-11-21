#3 Write a program that prints the multiplication table(from 1 to 10) for numbers
#  from 1-5 using nested for loops.
# Solution
for i in range(1, 6):
    print(f"Multiplication table for {i}:")
    for j in range(1, 11):  
        print(f"{i} x {j} = {i * j}")
    print()  
