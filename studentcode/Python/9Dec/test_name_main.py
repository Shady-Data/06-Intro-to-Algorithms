# before python runs any code it sets special variables, when it runs a file
# directly it sets __name__ to main.

# print(f'Original File: {__name__}')

if __name__ == '__main__':
    print(f'Original File: {__name__}')
else:
    print(f'not in main')