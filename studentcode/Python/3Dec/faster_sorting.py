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
******************** Quick Sort ********************

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

'''
******************** Merge Sort ********************

- Divide and Conquer strategy
- Compute the middle position of a list and recursively sort its left and right sublists
- Merge the two sorted sublists back into a single sorted list
- Stop the process when sublists can no longer be subdivided
'''

from array import array

def mergeSort(my_list):
    # copyBuffer temporary space needed during merge
    copyBuffer = array(len(my_list))
    mergeSortHelper(my_list, copyBuffer, 0, len(my_list) - 1)

# my_list       list being sorted
# copyBuffer    temp space needed during merge
# low, high     bounds of sublist
# middle        midpoint of sublist
def mergeSortHelper(my_list, copyBuffer, low, high):
    if low < high:
        middle = (low + high) // 2
        mergeSortHelper(my_list, copyBuffer, low, middle)
        mergeSortHelper(my_list, copyBuffer, middle + 1, high)
        merge(my_list, copyBuffer, low, middle, high)

# my_list        list that is being sorted
# copyBuffer     temp space needed during the merge process
# low            beginning of first sorted sublist
# middle         end of first sorted sublist
# middle + 1     beginning of second sorted sublist
# high           end of second sorted sublist
# Initialize     i1 and i2 to the first items of second sorted sublist
# The merge function combines two sorted sublists into a larger sorted sublist
# The first sublist lies between low and middle and the second between middle + 1 and high
# - Set up index pointers to the first items in each sublist. These are low and middle + 1
# - Starting with the first item in each sublist, repeatedly compare items. Copy the smaller item
#   from its sublist to the copyBuffer and advance to the next item in the sublist.
# - Copy the portion of copyBuffer between low and high back to the corresponding positions in my_list
def merge(my_list, copyBuffer, low, middle, high):
    i1 = low
    i2 = middle + 1
    # Put items from sublists into copyBuffer so order is maintained
    for i in range(low, high +1):
        if i1 > middle:
            # First sublist exhausted
            copyBuffer[i] = my_list[i2]
            i2 += 1
        elif i2 > high:
            # Second sublist exhausted
            copyBuffer[i] = my_list[i1]
            i1 +=  1
        elif my_list[i1] < my_list[i2]:
            copyBuffer[i] = my_list[i1]
            i1 += 1
        else:
            copyBuffer[i] = my_list[i2]
            i2 += 1
    # Copy sorted items back to proper position in the list
    for i in range(low, high + 1):
        my_list[i] = copyBuffer[i]
        