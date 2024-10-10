a = [7, 5, 4, 3, 8, 9]
b = []

max = 0

def find_largest(l, max):
    for i in l:
        if i >= max:
            max = i
    return max

largest_number = find_largest(a, max)

def skip_largest(src_list, tgt_list):
    for j in src_list:
        if j == largest_number:
            continue
        else:
            tgt_list.append(j)

skip_largest(a, b)

second_larget = find_largest(b, max)
print(f"second_larget number: {second_larget}")
a = b
b = []
largest_number = find_largest(a, max)
skip_largest(a, b)
third_larget = find_largest(b, max)
print(f"third_larget number: {third_larget}")
