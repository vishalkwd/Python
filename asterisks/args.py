'''
Usage of * :-
- Multiplication (2 * 3 = 6)
- Exponentiation (2 ** 3 = 8)
- Multiplication of a list (['a'] * 3 -> ['a', 'a', 'a'])

- Unpacking a function using positional argument
- Passing a function using * with an arbitrary number of positional arguments
- Passing a  Function Using with an arbitrary number of keyword arguments
'''
# -------------------------------------------------------------------------------------------------
# Unpacking a function using positional argument:
# arr = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
# print(' '.join(map(str, arr))) # just converting items to string
# print(*arr)
# -------------------------------------------------------------------------------------------------


def addition(*args) -> int:
    return sum(args)
# sum([1, 2, 3, 4, 5]) # this one works. sum accepts a list to add everything. Meaning, * treats
# the argument as a list and needs a list

print(addition(1, 2, 3, 4))