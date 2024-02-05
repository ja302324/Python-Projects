
# .insert adds number at the specified index in the list. If no index is given it will insert at the end of the list. The function returns None.
# .append () method is used to add an element at the end of a list
# .pop () method is used to remove an element from the last position in a list (default value for pop
# .count () method returns the number of times a specified value appears in a list
# .sort () sorts the elements of a given list in a specific order (ascending or descending)
# .reverse  () reverses the elements of a given list
# .copy () makes a copy of the original list and returns it

numbers = [2, 5, 3, 7, 2, 8, 4, 2, 1, 7, 8, 5]
numbers2 = []

for item in numbers:
    if item not in numbers2:
        numbers2.append(item)

print(numbers2)
