problems = 'too, cool, to, handle'
print(problems)

# The split() method splits a string into a list.
# string.split(separator, maxsplit(o)) #TO make a list from string

l = problems.split(",")  # to make a list
print(l)

l2 = problems.split(", ")
print(l2)

# join function make a string
joined = " richa is".join(l)
print(joined)

txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 3 elements!
x = txt.split("#", 2)

print(x)
