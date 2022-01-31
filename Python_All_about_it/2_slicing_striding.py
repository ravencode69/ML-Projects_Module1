digits = [98, 1, 2, 3, 4, 5, 6, 7, 8]

# negative indexing
print(digits[-1])
print(digits[-3])
print(digits[-len(digits)])

# range #slicing ;- get any chunk startingpoint:endpoint
# 0 if starting point not given startpoint is inclusive but end #point is exclusive
print(digits[2:4])
print(digits[1:-1])

# striding start:end:jumplen
print(digits[0:-1:2])

print(digits[-1:-4:-2])  # careful with negative jump it is from left
