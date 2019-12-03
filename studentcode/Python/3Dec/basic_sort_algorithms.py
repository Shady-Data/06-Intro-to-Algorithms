'''
Basic Sort Algorithms

    The algorithms examined here are easy to write but are inefficient
    Each algorithm we discuss here will utilize a list of integers and the
    swap function defined below
'''
from random import randint

# The swap function
def swap(my_list, i, j):
    # exchanges the positions of i and j
    temp = my_list[i]
    my_list[i] = my_list[j]
    my_list[j] = temp

# ******************** Selection Sort ********************
# Each pass through the main loop selects a single item to be moved
# Searches the list for the position of the smallest item
# If that position is not the first position it swaps the items at those positions
# It then finds the next smallest item and swaps the item of the second position and so on

def selectionSort(my_list):
    i = 0
    # swaps = 0
    # do n-1 searches for the smallest
    while i < len(my_list) -1:
        minIndex = i
        j = i + 1
        # start the search
        while j < len(my_list):
            if my_list[j] < my_list[minIndex]:
                minIndex = j
            j += 1
        # Exchange if needed
        if minIndex != i:
            swap(my_list, minIndex, i)
            # swaps += 1
        i += 1
    # print(swaps)

'''
(n-1) + (n-2) + ... + 1 =
n(n-1)/2 =
(1/2)n^2 - (1/2)n

O(n^2)

Because data items swap only in the outer loop, this additional cost for selection sort is linear in the worst and average cases.
'''

# ******************** Bubble Sort ********************
# The strategy is to start at the beginning of the list and compare pairs of data items as it moves down to the end.
# Each time the items in the pair are out of order, the algorithm swaps them.
# The largest item will eventually "bubble" out to the end of the list.
# The algorithm repeats this process until the list is sorted from smallest to largest


# def bubbleSort(my_list):
#     n = len(my_list)
#     # Do n - 1 bubbles
#     while n > 1:
#         i = 1
#         # Start each bubble
#         while i < n:
#             if my_list[i] < my_list[i - 1]:  
#                 # Exchange if needed
#                 swap(my_list, i, i - 1)
#             i += 1
#         n -= 1

'''
(1/2)n^2 - (1/2)n

O(n^2)

'''

# Update bubble sort to linear time complexity
# In our best case scenario where are list is already sorted, there are no swaps
# so we can modify our algorithm to be more efficient
def bubbleSort(my_list):
    n = len(my_list)
    # do n - 1 searches
    # swaps = 0
    while n > 1:
        swapped = False
        i = 1
        # start each bubble
        while i < n:
            if my_list[i] < my_list[i - 1]:
                # Exchange if needed
                swap(my_list, i, i - 1)
                swapped = True
                # swaps += 1
            i += 1
            # return if no swaps
        if not swapped:
            # print(swaps)
            return
        n -= 1
    # print(swaps)

# the_list = [randint(1,100) for x in range(10)]
# print(the_list)
# selectionSort(the_list)
# print(the_list)

# the_other_list = [randint(1,100) for x in range(10)]
# print(the_other_list)
# bubbleSort(the_other_list)
# print(the_other_list)

# ******************** Insertion Sort ********************
# - On the ith pass through the list, where i ranges from 1 to n-1, the ith
#   item should be inserted into its proper place among the first i items in the list
# - After the ith pass, the first i items should be in sorted order
# - This process is analogous to the way in which many people organize playing cards
#   in their hands. That is, if you hold the first i-1 cards in order,
#   you pick the ith card and compare it to these cards until its proper spot is found
# - Insertion sort consists of two loops. The outer loops traverses the positions
#   from 1 to n-1. For each position i in this loop, you save the item and start
#   the inner loop at position i-1 . for each j position in this loop, you move the item
#   to position j+1 until you find the insertion point for the saved(ith) item
# - Insertion sort is good for partially sorted lists due to the inner loop

def insertionSort(my_list):
    i = 1
    while i < len(my_list):
        itemToInsert = my_list[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < my_list[j]:
                my_list[j + 1] = my_list[j]
                j -= 1
            else:
                break
        my_list[j + 1] = itemToInsert
        i += 1

'''
(1/2)n^2 - (1/2)n

O(n^2)

'''