# they are really good for : 1. super organized data(mini databases) 2. Fast AF const. time
# they are now ordered by default for pyth 3.7 and later
dict = {'bananas': 3, 'oranges': 5}  # key value pair

print(dict['bananas'])
print(dict.get('hello'))  # None
# any name any data ko map kr skte h

dict4 = {'hanna': [21, 'oranges', bool(1)],
         'maddy': [23, 'funfru', bool(0)],
         'everj': [32, 'loops', bool(1)]

         }

print(list(dict4.values()))  # casted the values of the dict to list

print(dict4['maddy'])
print(dict4.items())
print(list(dict4.keys()))  # can cast into list
print(dict4.values())


# deletion
# dict4.pop('hanna')
# print(dict4.values())

# deletion of LAST ELEMENT
print(dict4.popitem())
print(dict4)

dict.clear()
