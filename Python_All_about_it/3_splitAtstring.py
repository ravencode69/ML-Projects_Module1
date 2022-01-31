problems = 'too, cool, to, handle'
print(problems)

# Split a string into a list where each word is a list item:
#string.split(separator, maxsplit(o))

l = problems.split(",")
print(l)

l2 = problems.split(", ")
print(l2)

# join function
joined = "richa is".join(l)
print(joined)

txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 2)

print(x)
