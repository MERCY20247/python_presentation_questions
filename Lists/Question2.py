#2) Write a function that takes a list of numbers and returns a new list with each number squared. 
# Example: [1,2,3] should become [1,4,9]
#Solution:
def square_numbers(numbers):
    return [num ** 2 for num in numbers]
numbers = [1, 2, 3]
squared = square_numbers(numbers)
print(squared)
  