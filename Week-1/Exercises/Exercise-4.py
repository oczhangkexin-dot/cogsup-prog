################################################################################
"""
Recommended readings: 
  Chapter on dictionaries: https://automatetheboringstuff.com/3e/chapter7.html 
  Iterating through dictionaries: https://realpython.com/iterate-through-dictionary-python/
"""
################################################################################

"""
Exercise 4.1

Task:
------
Print the sum of the values in the dictionary.
"""

dct = {'a': 3, 'b': 7, 'c': -2, 'd': 10, 'e': 5}

print("Exercise 4.1")

pass

sum = 0
for i in dct:
  sum += dct[i]
print(sum)

"""
Exercise 4.2

Task:
------
Print the key that has the largest value in dct.
"""

print("Exercise 4.2")

pass

print(max(dct.values()))

"""
Exercise 4.3

Task:
------
Create a new dictionary with the squares of all the values in dct.
"""

print("Exercise 4.3")

pass

dct2 = {}
for i in dct:
  dct2[i] = dct[i] ** 2
print(dct2)

"""
Exercise 4.4

Task:
------
Print only the keys in dct whose values are even numbers.
"""

print("Exercise 4.4")

pass

even = []
for i in dct:
  if dct[i] % 2 == 0:
    even.append(i)
print(even)

"""
Exercise 4.5

Task:
------
Create a new dictionary that swaps the keys and values in dct.
"""

print("Exercise 4.5")

pass

dct3 = {}
for key, value in dct.items():
  dct3[value] = key
print(dct3)

"""
Exercise 4.6

Task:
------
Count the number of times each letter appears in the string 'ccctcctttttcc'
and print the resulting dictionary.
"""

s = 'ccctcctttttcc'

print("Exercise 4.6")

pass

dict4 = {}
for i in s:
  dict4[i] = s.count(i)
print(dict4)

"""
Exercise 4.7

Task:
------
Given the dictionary of responses_mapping = {'j':'jazz', 'p':'pop'},
and the string responses = 'jjjpjjpppppjj',
print the list of corresponding words.
"""

responses_mapping = {'j':'jazz','p':'pop'}
responses = 'jjjpjjpppppjj'

print("Exercise 4.7")

pass

lst = []
for i in responses:
  lst.append(responses_mapping[i])
print(lst)

"""
Exercise 4.8

Task:
------
Merge the following two dictionaries into one:
{'a': 1, 'b': 2} and {'c': 3, 'd': 4}
"""

print("Exercise 4.8")

pass

dct5 = {'a': 1, 'b': 2}
dct6 = {'c': 3, 'd': 4}
dct5.update(dct6.items())
print(dct5)

"""
Exercise 4.9

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose keys are sorted alphabetically.
"""

print("Exercise 4.9")

pass

dct_anim = {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9}
sorted_by_keys = {}
for i in sorted(dct_anim):
  sorted_by_keys[i] = dct_anim[i]
print(sorted_by_keys)

"""
Exercise 4.10

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose values appear in increasing order.
"""

print("Exercise 4.10")

pass

sorted_by_values = {}

def value_key(x):
  return x[1]

for key, value in sorted(dct_anim.items(), key=value_key):
  sorted_by_values[key] = value

print(sorted_by_values)

