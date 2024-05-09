import re


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)
with open("dictionary.txt", "r") as file:
    dictionary_list = file.read().splitlines()
print("Method of sort: Linear")

line_number = 0
with open("AliceInWonderLand200.txt", "r") as file:
    for line in file:
        line_number += 1
        word_list = split_line(line)
        for word in word_list:
            word_upper = word.upper()
            if word_upper not in dictionary_list:
                print(f"Line {line_number}: {word}")

print("Method of sort:Binary")
with open("AliceInWonderLand200.txt", "r") as file:
    line_number = 0
    for line in file:
        line_number += 1
        word_list = split_line(line)
        for word in word_list:
            word_upper = word.upper()
            low = 0
            high = len(dictionary_list) - 1
            found = False
            while low <= high and not found:
                mid = (low + high) // 2
                if dictionary_list[mid] == word_upper:
                    found = True
                elif dictionary_list[mid] < word_upper:
                    low = mid + 1
                else:
                    high = mid - 1
            if not found:
                print(f"Line {line_number}: {word}")

