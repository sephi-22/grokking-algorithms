# Function to get smallest item in a list.


def find_smallest_index(list):
    smallest = list[0]
    smallest_index = 0
    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i
    return smallest_index


# Selection sort function as given in the book


def selection_sort(list):
    sorted_list = []
    for i in range(len(list)):
        smallest_index = find_smallest_index(list)
        sorted_list.append(list.pop(smallest_index))
    return sorted_list


# Selection sort function that does not change original list. Using one loop.
# This is not a very graceful solution


def selection_sort_no_pop(list):
    x = 0
    for i in range(len(list)):
        smallest_index = find_smallest_index(list[i:])
        list[i], list[smallest_index + x] = list[smallest_index + x], list[i]
        x += 1
    return list


# Both minimum index and selection sort together in one function


def selection_sort_combined(list):
    for i in range(len(list)):
        smallest_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[smallest_index]:
                smallest_index = j
        list[i], list[smallest_index] = list[smallest_index], list[i]
    return list


# Recursive implementation. Not recommended. Not for practical cases
# Uses an additional parameter called start index


def selection_sort_recursive(list, start_index=0):
    if start_index == len(list) - 1:
        return 1
    smallest_index = start_index
    for i in range(start_index + 1, len(list)):
        if list[i] < list[smallest_index]:
            smallest_index = i
    list[smallest_index], list[start_index] = list[start_index], list[smallest_index]
    selection_sort_recursive(list, start_index + 1)
    return list


# Test Case

myList = [4, 5, 6, 3, 4, 2, 1, 3, 4, 5, 6, 8, 3, 9]
print(selection_sort_recursive(myList))

# This has O(n^2) complexity
