# Given a number print the number as text
# Example : 345  is three hundred forty five
# 4898848 :   Four million eight hundred ninety eight thousand eight hundred forty eight

a = 345

num_length = len(str(a))

total_groups = num_length//3

num_dict_single = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "10"}
num_dict_double = {10, 11, 12, 20, 30, 40, 50, 60, 70, 80, 90, 100}

def group_text(num):
    pass