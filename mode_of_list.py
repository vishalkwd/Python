# Mode of a dataset is the item that occurs the maximum number of times in the dataset.
# Given A = [3, 3, 5, 5, 5 , 6, 9, 9 , 1 , 4 , 4, 3,  11, 12, 13 ]
# The mode of A  [3, 5] because both 3 and 5 occur 3 times each
# Given B = [3, 3, 5, 5, 5 , 6, 9, 9 , 1 , 4 , 4, 3,  11, 12, 13 , 3]
# The mode of B is just [3]
# Question : given an array , print the mode

A = [3, 3, 5, 5, 5 , 6, 9, 9 , 1 , 4 , 4, 3,  11, 12, 13 ]
# A = [3, 3, 5, 5, 5 , 6, 9, 9 , 1 , 4 , 4, 3,  11, 12, 13 , 3]
unique_keys = set(A)

result = {}
final_list = []
max_val = 0

for key in A:
    if key in result:
        result[key] += 1
    else:
        result[key] = 0

for key, val in result.items():
    if val >= max_val:
        max_val = val
        final_list.append(key)

print(final_list)
