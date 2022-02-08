
l1 = ['Rachel Green', 'Georgia Miller', 'Alex Vause']

# list comprehension : simple one line of code

print([person+' is my crush' for person in l1])

d = {'Alex': 9,
     'Rachel': 8,
     'Georgia': 10}

print([person for person in d if d[person] > 8])
