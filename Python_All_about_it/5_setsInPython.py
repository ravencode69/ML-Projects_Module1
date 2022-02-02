# cant have any duplicates also unordered - cant iterate
set2 = {"hello my name is richa", "i hope you're fine"}
set2.add("sunflower")
set2.add("sunflower")
# print(set2)

l = [1, 2, 2, 2, 4, 5, 6, 7]

no_duplicate = set(l)  # made list a set to remove duplicates
print(no_duplicate)
no_duplicate = list(no_duplicate)  # casting back to list
print(no_duplicate)

# The set() Constructor It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)
