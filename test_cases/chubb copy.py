values = '000101000010000000000000010'
keys = 'abcdefghijklmnopqrstuvwxyz'

map_dict = { key: val for key, val in zip(keys, values) }
# map_dict_2 = dict(map(lambda x, y: (x, y), keys, values))
# map function -> map(function, iterable)

k = 2
string = 'abcd'

a = sum([int(map_dict.get(i)) for i in string])
if a == 1:
    print("Prime word")
else:
    print("Standard")