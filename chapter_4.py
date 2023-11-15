# add up all the numbers in an array using loop
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total


# Try this using a recursive function
def sum_recursive(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum_recursive(arr[1:])


# Alternate way of using a recursive function (book)
# This is a better method since it handles the case when an empty array is passed.
def sum_recursive_book(arr):
    if arr == []:
        return 0
    return arr[0] + sum_recursive(arr[1:])


# Try this using a recursive function (initial method)
# This is adding last element towards first element. Others are adding first element onwards
def sum_recursive_initial(arr):
    last_index = len(arr) - 1
    if last_index == 0:
        return arr[0]
    last_ele = arr[last_index]
    return last_ele + sum_recursive(arr[:last_index])


# Recursive function to count the number of items in a list.
def count_items(arr):
    if arr == []:
        return 0
    return 1 + count_items(arr[1:])


# Find the maximum number in a list (book method)
def find_max(arr):
    if len(arr) == 2:  # Base Case
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = find_max(arr[1:])  # Recursive case
    return arr[0] if arr[0] > sub_max else sub_max


# Find the maximum number in a list (initial method)
# Not recommended since it changes the list. We remove elemets till we only get the max element left
def find_max_initial(arr):
    if len(arr) == 1:
        return arr[0]
    if arr[0] > arr[1]:
        arr.pop(1)
    else:
        arr.pop(0)
    return find_max_initial(arr)


# Binary search using recursive
def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


# Quicksort algorithm
def quicksort(arr):
    if len(arr) < 2:
        return arr  # Base Case
    else:
        pivot = arr[0]  # Recursive case
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


# Quicksort with random pivot
def quicksort_random(arr):
    if len(arr) < 2:
        return arr  # Base Case
    else:
        pivot = arr[len(arr) // 2]  # Choosing a pivot
        left = [i for i in arr if i < pivot]
        middle = [i for i in arr if i == pivot]
        right = [i for i in arr if i > pivot]
        return quicksort(left) + middle + quicksort(right)


# Testing
myArray = [45, 2, 67, 54, 23, 37, 89, 100, 9, 76]
print(quicksort(myArray))
print(quicksort_random(myArray))

# Test Cases
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 36, 37, 78]
print(binary_search_recursive(myList, 37))
