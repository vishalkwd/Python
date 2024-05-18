from itertools import permutations, combinations
values = '000101000010000000000000010'
keys = 'abcdefghijklmnopqrstuvwxyz'

map_dict = dict(map(lambda x, y: (x, y), keys, values))
k = 2
string = 'giraffe'
sub_dict = {k: int(map_dict.get(k)) for k in string}
