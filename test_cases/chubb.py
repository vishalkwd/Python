def intelligent_substring(s, k, char_set):
    from itertools import permutations, combinations
    keys = 'abcdefghijklmnopqrstuvwxyz'

    map_dict = dict(map(lambda x, y: (x, y), keys, char_set))
    temp_out = []
    for total_chars in range(1, len(s)+1, 1):
        for word_tuples in permutations(s, total_chars):
            zero_counter = 0
            if ''.join(word_tuples) in s:
                for letter in word_tuples:
                    if int(map_dict.get(letter)) == 0:
                        zero_counter += 1
                if zero_counter == k:
                    temp_out.append(len(''.join(word_tuples)))
    if len(temp_out) == 0:
        return 0
    else:
        return max(temp_out)

k = 2
char_set = '100000000010000000000000010'
s = 'giraffe'

print(intelligent_substring(s, k, char_set))