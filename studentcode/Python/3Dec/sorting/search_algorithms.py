'''
************** Search Algorithms **************

'''
# ************** Search for the minimum **************
# This function mimics Python's min() function
# Use this function to study the complexity of this algorithm
# by returning the index of the minimum item
# This algorithm assumes that the list is not empty and that the
# items are not in a specific order
# This algorithm starts by treating the first position as that of the
# minimum item. It then searches to the right for a smaller item,
# and if found, resets the position of min to the current position
# when it reaches the end of the list it returns the position of the min item
def index0fmin(my_list):
    """Returns the index of the minimum item."""
    minIndex = 0 
    currentIndex = 1
    while currentIndex < len(my_list):
        if my_list[currentIndex] < my_list[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return minIndex

# the_list = [2, 6, 5, 1, 3, 4, 9]
# print(index0fmin(the_list))

# ************** Sequential Search **************
# This function returns the position of the target item it found, or -1 otherwise

def seqSearch(target, my_list):
    """Returns the position of the target item if found, or -1 otherwise."""
    position = 0
    while position < len(my_list):
        if target == my_list[position]:
            return position
        position += 1
    return -1

# the_list = [2, 6, 5, 1, 3, 4, 9]
# print(seqSearch(2, the_list))

# You can sometimes have a best, worst, average case performance
# however you usually don't want to use the best case performance, focus
# on the average and worst cases.

# ************** Binary Search of a Sorted List **************
# Used to search an ordered list for a particular value
# Divide and conquer approach
# Target compared with middle value, then half of the list is 'discarded', repeatedly, until the target is found
# Very efficient for large sorted lists

def binarySearch(target, sortedList):
    left = 0
    right = len(sortedList) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if target == sortedList[midpoint]:
            return midpoint
        elif target < sortedList[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1

my_list = [1,2,3,4,5,6,7,8,9]
print(binarySearch(3, my_list))

"""
For a list of size n we perform the reduction n/2/2/2... until we get to 1

Let k be the number of times we divide n by 2 then we get
    n/2^k = 1
    n = 2^k
    k = log base 2 of n
"""