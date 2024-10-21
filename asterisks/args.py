'''
Usage of * :-
- Multiplication (2 * 3 = 6)
- Exponentiation (2 ** 3 = 8)
- Multiplication of a list (['a'] * 3 -> ['a', 'a', 'a'])

- Unpacking a function using positional argument
- Passing a function using * with an arbitrary number of 'positional arguments' (*args)
- Passing a  Function Using with an arbitrary number of 'keyword arguments' (**kwargs)

- * treats passed arguments as list
- ** treats passed arguments as dictionary

- *args = positional arguments
- **kwargs = keyword arguments

Note: Uncomment individual code block to execute
'''

# Unpacking a function using positional argument:
# -------------------------------------------------------------------------------------------------
# arr = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
# print(' '.join(map(str, arr))) # just converting items to string
# print(*arr)
# -------------------------------------------------------------------------------------------------

# Passing a function using * with an arbitrary number of positional arguments
# -------------------------------------------------------------------------------------------------
# def addition(*args) -> int:
#     '''
#     This is sample docstring and can be printed using addition.__doc__()'''
#     return sum(args)
# # sum([1, 2, 3, 4, 5]) # this one works. sum accepts a list to add everything. Meaning, * treats
# # the argument as a list and needs a list
# print(addition(1, 2, 3, 4, 4))
# -------------------------------------------------------------------------------------------------

# Passing a  Function Using with an arbitrary number of keyword arguments
# -------------------------------------------------------------------------------------------------
# # first example with food called with keyword items and second with dictionary
# def food(**kwargs):
#     for item in kwargs:
#         print(f"{kwargs[item]} is a {item}")
# 
# food(fruit = 'cherry', vegie = 'spinach')
# # or
# dict = {'fruit': 'cherry', 'vegie': 'potato', 'boy': 'john'}
# food(**dict)
# -------------------------------------------------------------------------------------------------