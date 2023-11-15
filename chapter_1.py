# Binary Search Algorithm
def binary_search(list, element):
    first = 0
    last = len(list) - 1
    while first <= last:
        middle = (first + last) // 2
        if list[middle] < element:
            first = middle + 1
        elif list[middle] > element:
            last = middle - 1
        else:
            return middle


myList = [1, 3, 5, 7, 8, 9, 11, 13, 15, 17, 19]
print(binary_search(myList, 9))
