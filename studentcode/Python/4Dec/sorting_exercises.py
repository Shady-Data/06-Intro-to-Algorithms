"""
1. The list method .reverse() reverses the elements in the list. Define a function named reverse that 
reverses the elements in its list argument (without using the method reverse). Try to make this 
function as efficient as possible, and state its computational complexity using big-O notation. 

- Questions: Does this need to return a new list, or mutate the list passed in
​"""

import timeit
from random import randint

def reverse_mutate_list(p_list):
    # This funtion mutates a list passed in by reversing the order of the lists elements (i.e. list[0] is swapped with list[len(list)-1])
    i = 0
    while i < len(p_list)//2:
        # set variable j to be the last viable index, decrementing by the same value that i increments
        j = len(p_list) - (1 + i)
        # store one of the elements in a temp variable (j for this program)
        temp = p_list[j]
        # set the element stored with its opposite element index (i for the program)
        p_list[j] = p_list[i]
        # set the other element's value with the temp variable's value
        p_list[i] = temp
        # increment i for the next index's work
        i += 1

    # Big-O: O(n)


def reverse_new_list(p_list):
    # This funtion returns a new list passed in by reversing the order of the lists elements (i.e. list[0] is swapped with list[len(list)-1])
    return [p_list[i] for i in range(len(p_list) - 1, -1, -1)]
    # Big-O: O(n)

# sanity check
# the_list = [randint(1, 100) for _ in range(20)]
# print(f'Original list:\t{the_list}')
# print('Reversed new list:\t', reverse_new_list(the_list))
# print(f'Before mutation:\t{the_list}')
# reverse_mutate_list(the_list)
# print(f'After mutation:\t{the_list}')

"""
2. Python’s pow function returns the result of raising a number to a given power. Define a function 
expo that performs this task and state its computational complexity using big-O notation. The first 
argument of this function is the number, and the second argument is the exponent (nonnegative numbers only). 
You can use either a loop or a recursive function in your implementation, but do not use Python’s ** operator 
or pow function. 
"""
# recursive
def expo(p_num, p_expo):
    # if the exponent is 0
    if p_expo == 0:
        # return 1
        return 1
    # if the exponent is 1
    elif p_expo == 1:
        # return the number
        return p_num
    # otherwise
    else:
        # return the number * the recursive call, decrementing the exponent by 1 for each successive call
        return p_num * expo(p_num, p_expo - 1)

    # Big-O: O(n)

# sanity check
# print(expo(2, 4))
# print(2**4)
# print(pow(2,4))

setup_new_list ='''def reverse_new_list(p_list):
    return [p_list[i] for i in range(len(p_list) - 1, -1, -1)]

my_list = [38, 55, 23, 74, 62, 54, 37, 28, 29, 52, 6]
print(my_list)
print(reverse_new_list(my_list))
'''
setup_mut_list ='''def reverse_mutate_list(p_list):
    i = 0
    while i < len(p_list)//2:
        j = len(p_list) - (1 + i)
        temp = p_list[j]
        p_list[j] = p_list[i]
        p_list[i] = temp
        i += 1

my_list = [45, 77, 65, 16, 86, 40, 37, 99, 64]
print(my_list)
reverse_mutate_list(my_list)
print(my_list)
'''


setup_expo1 = '''def expo(p_num, p_expo):
    if p_expo == 1:
        return p_num
    else:
        return p_num * expo(p_num, p_expo - 1)

print(f"{expo(2, 4):,}")
'''
setup_expo2 = '''def expo(p_num, p_expo):
    if p_expo == 1:
        return p_num
    else:
        return p_num * expo(p_num, p_expo - 1)

print(f"{expo(2, 8):,}")
'''
setup_expo3 = '''def expo(p_num, p_expo):
    if p_expo == 1:
        return p_num
    else:
        return p_num * expo(p_num, p_expo - 1)

print(f"{expo(2, 16):,}")
'''
setup_expo4 = '''def expo(p_num, p_expo):
    if p_expo == 1:
        return p_num
    else:
        return p_num * expo(p_num, p_expo - 1)

print(f"{expo(2, 32):,}")
'''
setup_expo5 = '''def expo(p_num, p_expo):
    if p_expo == 1:
        return p_num
    else:
        return p_num * expo(p_num, p_expo - 1)

print(f"{expo(2, 64):,}")
'''

print(f'Rev New list:    {timeit.timeit(setup=setup_new_list, number=10000000):.5f}')
print(f'Rev Mutate list: {timeit.timeit(setup=setup_mut_list, number=10000000):.5f}')
print(f'Expo 2, 4:       {timeit.timeit(setup=setup_expo1, number=10000000):.5f}')
print(f'Expo 2, 8:       {timeit.timeit(setup=setup_expo2, number=10000000):.5f}')
print(f'Expo 2, 16:      {timeit.timeit(setup=setup_expo3, number=10000000):.5f}')
print(f'Expo 2, 32:      {timeit.timeit(setup=setup_expo4, number=10000000):.5f}')
print(f'Expo 2, 64:      {timeit.timeit(setup=setup_expo5, number=10000000):.5f}')