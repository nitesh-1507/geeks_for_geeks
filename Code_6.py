# Program to manipulate string

import string
import collections
stored_string = 'helloooo'

# program to remove duplicate characters in string

unique = []
for i in stored_string:
    if i not in unique:
        unique.append(i)

print(unique)


# program to covert the repeated characters to uppercase
new_string = list(stored_string)
string_dict = collections.Counter(new_string)

for i in string_dict.keys():
    if string_dict[i] > 1:
       index = [j for j, x in enumerate(new_string) if x == i]
       for k in index:
           new_string[k] = i.upper()

print(new_string)

# program to imitate collection.Counter()
character_dict = {}

for i in set(stored_string):
    character_dict[i] = len([j for j, x in enumerate(stored_string) if x == i])

print(character_dict)
