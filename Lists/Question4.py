#4) Given a list of numbers, [3,1,4,5,9,2], write a program to find and print the two largest numbers
# in the list without using the max() function.
#Solution:
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers, reverse=True)
two_largest = sorted_numbers[:2]
print(two_largest)  
