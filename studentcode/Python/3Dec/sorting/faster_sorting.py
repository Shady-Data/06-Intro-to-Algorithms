'''
Faster Sorting

Up until now we've learned about sorting methods with a O(n^2) complexity. Even with modifications they are only marginally faster

Let's now discuss some algorithms with a complexity of O(log n) or O(n log n)
The secret here is that we use our "divide and conquer" strategy
Each algorithm finds a way of breaking the list into smaller lists. Then these sublists are sorted recursively.
The number of subdivisions is log(n) and the amount of work needed to rearrange the data on each subdivision is n,
thus making our complexity O(n log n)
'''

'''
******************** Selection Sort ********************

- The strategy here is that we start with a PIVOT. Pivot can be anywhere but lets just start
    by setting our pivot to the midpoint.
- Partition items in the list so that all items less than the pivot are moved to the left of the pivot, and the rest
    are moved to its right. The final position of the pivot after the list is sorted could be at the end of the list
    or the beginning of the list depending on the size of the item.
- Divide and Conquer. Reapply the process recursively to the sublists formed by splitting the list at the pivot.
    One sublist consists of all items to the left of the pivot (now the smaller ones), and the other sublist has all
    items to the right (larger items).
- The process terminates each time it encounters a sublist with fewer than two items
'''

# helper_calls = 0
# swaps = 0

def quicksort(my_list):
    quicksortHelper(my_list, 0, len(my_list) - 1)

# recursive function to hide extra arguments for the endpoints of a sublist
def quicksortHelper(my_list, left, right):
    # global helper_calls
    if left < right:
        # helper_calls += 1
        pivotLocation = partition(my_list, left, right)
        # recursively calls quicksortHelper for the left of the partition
        quicksortHelper(my_list, left, pivotLocation - 1)
        # recursively calls quicksortHelper for the right of the partition
        quicksortHelper(my_list, pivotLocation + 1, right)
        
def partition(my_list, left, right):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = my_list[middle]
    my_list[middle] = my_list[right]
    my_list[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if my_list[index] < pivot:
            swap(my_list, index, boundary)
            boundary += 1
    # Exchange the pivot item and the boundary item
    swap (my_list, right, boundary)
    return boundary

# The swap function
def swap(my_list, i, j):
    # global swaps
    # swaps += 1
    # exchanges the positions of i and j
    temp = my_list[i]
    my_list[i] = my_list[j]
    my_list[j] = temp
    # print('\t', my_list)

import random

def main(size = 20, sort_this = quicksort):
    # my_list = []
    my_list = [random.randint(1, size + 1) for _ in range(size)]
    # for _ in range(size):
    #     my_list.append(random.randint(1, size + 1))
    print(my_list)
    sort_this(my_list)
    print(my_list)
    # print(helper_calls)
    # print(swaps)
    

main()