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

# Inbuilt functions to manipulate strings

print(stored_string.upper())
print(stored_string.lower())
print(stored_string.islower())
print(stored_string.isupper())
print(len(stored_string))
print(stored_string.isalpha())
print(stored_string.isalnum())
print('-'.join(stored_string))
print('*'.join(stored_string))
print(stored_string.find('o'))
print(stored_string.capitalize())
print(stored_string.index('e'))
print(stored_string.endswith('o'))
print(stored_string.startswith('h'))
print(stored_string.count('o'))