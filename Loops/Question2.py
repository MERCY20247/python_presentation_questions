#2 Use a while loop to ask the user to input a number until they provide a number greater than 10.
while True:
    user_input = int(input("Please enter a number greater than 10: "))
    if user_input > 10:
        print("Thank you! You entered a valid number.")
        break
    else:
        print("The number is not greater than 10. Please try again.")