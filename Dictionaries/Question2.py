#2) Write a function that takes a dictionary of people's names and their ages,{'Alice': 24, 'Bob': 19, 'Charlie': 30}
#and returns a list of names of people who are 21 or older.
def required_ages(age_dict):
    return [name for name, age in age_dict.items() if age >= 21]
people = {'Alice': 24, 'Bob': 19, 'Charlie': 30}
eligible = required_ages(people)
print(eligible) 