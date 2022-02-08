# mutable :changeage
# dictonaries
# sets
# LISTS

# immutateable :unchangeable
# tuple
# string, int, float

# Lets consider a tuple
# here the list which is inside the tuple is actually mutable
t = (1, 2, 3, [5, 6, 7])

t[3][1] = 'R'
print(t)


# EVERYTHING IN PYTHON IS OBJECT
# which means every entity has some metadata (called attributes)
# and associated functionality (called methods). These attributes and methods are accessed via the dot syntax.
# in dictonaries for keys we can use keys so that they remain the same so that the dat do not get mixed up screwed up
