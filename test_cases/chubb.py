def intelligent_substring(values, k, string):
    """
    This function returns a dictionary with the keys being the letters of the alphabet
    and the values being their corresponding binary representations.
    """
    keys = 'abcdefghijklmnopqrstuvwxyz'

    if len(values) != 26:
        raise ValueError("The length of values must be 26.")

    map_dict = { key: val for key, val in zip(keys, values) }
    # map_dict_2 = dict(map(lambda x, y: (x, y), keys, values))
    # map function -> map(function, iterable)
    total = sum([int(map_dict.get(i)) for i in string])
    if total == k:
        print("Prime word")
    else:
        print("Standard")


# values = '000101000010000000000000010'
# k = 2
# string = 'abcd'
# map_dict = intelligent_substring(values, k, string)