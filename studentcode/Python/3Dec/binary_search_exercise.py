"""
1. Suppose that a list contains the values 20, 44, 48, 55, 62, 66, 74, 88, 93, 99 
at index positions 0 through 9. Trace the values of the variables left, right, and 
midpoint in a binary search of this list for the target value 90. Repeat for the 
target value 44.
​
value 99 = binary search return -1
    - first iteration midpoint = 4 left = 0 right = 9
​
"""

def binarySearch(target, sortedList):
    left = 0
    right = len(sortedList) - 1
    while left <= right:
        midpoint = (left + right) // 2
        # print(f'left = {left}')
        # print(f'right = {right}')
        # print(f'midpoint = {midpoint}')
        if target == sortedList[midpoint]:
            return midpoint
        elif target < sortedList[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1

# my_list = [1,2,3,4,5,6,7,8,9]
suppose_list = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]
#      indexqr:  0,  1,  2,  3,  4,  5,  6,  7,  8,  9
print(binarySearch(90, suppose_list))
'''
left = 0
right = 9
midpoint = 4
# midvalue = 62; leftvalues = [20, 44, 48, 55]; rightvalues = [66, 74, 88, 93, 99]; searched values[left:right] = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]
left = 5
right = 9
midpoint = 7
# midvalue = 88; leftvalues = [20, 44, 48, 55, 62, 66, 74]; rightvalues = [93, 99]; searched values[left:right] = [66, 74, 88, 93, 99]
left = 8
right = 9
midpoint = 8
# midvalue = 93; leftvalues = [20, 44, 48, 55, 62, 66, 74, 88]; rightvalues = [99]; searched values[left:right] = [93, 99]
-1
# 3 iterations before -1 return for not found
'''
print(binarySearch(44, suppose_list))
'''
left = 0
right = 9
midpoint = 4
# midvalue = 62; leftvalues = [20, 44, 48, 55]; rightvalues = [66, 74, 88, 93, 99]; searched values[left:right] = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]
left = 0
right = 3
midpoint = 1
# midvalue = 44; leftvalues = [20, 44, 48, 55]; rightvalues = [66, 74, 88, 93, 99]; searched values[left:right] = [20, 44, 48, 55]
1
# 2 iterations before position 1 return for the value 44
'''

'''
2(challenge). The method that’s usually used to look up an entry in a phone book is not 
exactly the same as a binary search because, when using a phone book, you don’t always go 
to the midpoint of the sublist being searched. Instead, you estimate the position of the 
target based on the alphabetical position of the first letter of the person’s last name. 
For example, when you are looking up a number for “Smith,” you look toward the middle of 
the second half of the phone book first, instead of in the middle of the entire book. 
Suggest a modification of the binary search algorithm that emulates this strategy for a 
list of names. Is its computational complexity any better than that of the standard 
binary search? 

# no, you would only remove to 2 loops of work, but add an initial check for start position
'''

print()

def binaryPhoneSearch(target, phoneList):
    # left = 0
    # right = len(phoneList) - 1
    if target.title()[0] < 'N':
        left = 0
        right = (len(phoneList) - 1)//2
    else:
        left = (len(phoneList) - 1)//2
        right = len(phoneList) - 1
    while left <= right:
        midpoint = (left + right) // 2
        # print(f'left = {left}')
        # print(f'right = {right}')
        # print(f'midpoint = {midpoint}')
        if target == phoneList[midpoint]:
            return midpoint
        elif target < phoneList[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1


part_phonebook_list = ['Adams', 'Brooks', 'Carter', 'Davids', 'Edwards', 'Fry', 'Goober', 'Hughes', 'Indra', 'Jones', 'Kerry', 'Lucas', 'Miller', 'Novas', 'Orkin', 'Phillips', 'Queens', 'Romero', 'Scott', 'Terry', 'Ulric', 'Victor', 'Williams', 'Xera', 'Yuri', 'Zora']
# indexqr = A:0, B:1, C:2, D:3, E:4, F:5, G:6, H:7, I:8, J:9, K:10, L:11, M:12, N:13, O:14, P:15, Q:16, R:17, S:18, T:19, U:20, V:21, W:22, X:23, Y:24, Z:25
print(binaryPhoneSearch("Orkin", part_phonebook_list))
'''
left = 12
right = 25
midpoint = 18
# midvalue = 'Scott'; searched values[left:right] = ['Miller', 'Novas', 'Orkin', 'Phillips', 'Queens', 'Romero', 'Scott', 'Terry', 'Ulric', 'Victor', 'Williams', 'Xera', 'Yuri', 'Zora']
left = 12
right = 17
midpoint = 14
# midvalue = 'Orkin'; searched values[left:right] = ['Miller', 'Novas', 'Orkin', 'Phillips', 'Queens', 'Romero']
14
'''
print(binaryPhoneSearch("Edwards", part_phonebook_list))
'''
left = 0
right = 12
midpoint = 6
# midvalue = 'Goober'; searched values[left:right] = ['Adams', 'Brooks', 'Carter', 'Davids', 'Edwards', 'Fry', 'Goober', 'Hughes', 'Indra', 'Jones', 'Kerry', 'Lucas', 'Miller']
left = 0
right = 5
midpoint = 2
# midvalue = 'Carter'; searched values[left:right] = ['Adams', 'Brooks', 'Carter', 'Davids', 'Edwards', 'Fry']
left = 3
right = 5
midpoint = 4
# midvalue = 'Edwards'; searched values[left:right] = ['Davids', 'Edwards', 'Fry']
4
'''
print(binaryPhoneSearch("Davis", part_phonebook_list))
'''
left = 0
right = 12
midpoint = 6
# midvalue = 'Goober'; searched values[left:right] = ['Adams', 'Brooks', 'Carter', 'Davids', 'Edwards', 'Fry', 'Goober', 'Hughes', 'Indra', 'Jones', 'Kerry', 'Lucas', 'Miller']
left = 0
right = 5
midpoint = 2
# midvalue = 'Carter'; searched values[left:right] = ['Adams', 'Brooks', 'Carter', 'Davids', 'Edwards', 'Fry']
left = 3
right = 5
midpoint = 4
# midvalue = 'Edwards'; searched values[left:right] = ['Davids', 'Edwards', 'Fry']
left = 3
right = 3
midpoint = 3
# midvalue = 'Davids'; searched values[left:right] = ['Davids']
-1
'''
print(binaryPhoneSearch("Terrance", part_phonebook_list))
'''
left = 12
right = 25
midpoint = 18
# midvalue = 'Scott'; searched values[left:right] = ['Miller', 'Novas', 'Orkin', 'Phillips', 'Queens', 'Romero', 'Scott', 'Terry', 'Ulric', 'Victor', 'Williams', 'Xera', 'Yuri', 'Zora']
left = 19
right = 25
midpoint = 22
# midvalue = 'Williams'; searched values[left:right] = ['Terry', 'Ulric', 'Victor', 'Williams', 'Xera', 'Yuri', 'Zora']
left = 19
right = 21
midpoint = 20
# midvalue = 'Ulric'; searched values[left:right] = ['Terry', 'Ulric', 'Victor']
left = 19
right = 19
midpoint = 19
# midvalue = 'Terry'; searched values[left:right] = ['Terry']
-1
'''
