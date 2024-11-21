#3) Write a Python program that takes two lists, list1 = [1,2,3] and list2 = [4,5,6] and combines them into
# a single list, combined = [1,4,2,5,3,6].
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = []
for x, y in zip(list1, list2):
    combined.append(x)
    combined.append(y)
print(combined) 