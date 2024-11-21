#4 Given a list of integers [4,7,2,9,12,15], write a program using a for loop to find the sum of all odd numbers and
# print the result.
#Solution:
numbers = [4, 7, 2, 9, 12, 15]
sum_of_odds = 0
for num in numbers:
    if num % 2 != 0: 
        sum_of_odds += num
print("The sum of all odd numbers is:", sum_of_odds)
