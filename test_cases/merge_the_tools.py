string = "AAABCADDE"
k = 3
start_index = 0
end_index = 0
for _ in range(int(len(string)/k)):
    end_index += k
    start_index = end_index - k
    print(''.join(list(dict.fromkeys(string[start_index: end_index]))))

# for word in word_list:
    # print(''.join(list(dict.fromkeys(word))))