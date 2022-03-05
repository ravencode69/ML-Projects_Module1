import re  # specify certain text

text = "reaLly3458 Something is here"

# it'll take a string in that describes out pattern and it will create a object in it and put it in pattern1
pattern1 = re.compile("something is here")

# res = pattern1.search(text)

# print(res)

pattern2 = re.compile("[a-zA-Z0-9]+")

# search func only find its first match and then it terminates
print(pattern2.search(text))
