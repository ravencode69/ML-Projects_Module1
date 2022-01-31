# functions in python
def func():
    if 5 == 5:
        print("hello")
    else:
        print("go")

# Integers
# float
# string - sentences "yo are you" 'A'
# bool- true or false

# ctrl+k ctrl+c, ctrl+k ctrl+u commenting stuff


# casting : from one data typr to another data type
x = 1
print(float(x))
print(str(x))
print(int("1"))
print(bool(0))

# strings in pyton //sentence that is together
str = "hello strings"
print(str[1])
print(str)

# List in python: hold bunch of things in order
l = [1, 2, 3]
# can add diffrent datatype in side the list
l2 = [1, "string", 4, 4.3, [2, 3]]
print(l2)
print(l2[4])

# adding element at the end of the list
names = ['richa', 'gary', 'turtle']
names.append('fools')
print(names)

# adding at the any location
names.insert(0, 'well')
print(names)
names.remove('gary')  # removing element from a list
print(names)

# Reverse a list
names.reverse()
print(names)
# sort a list
num = [7, 12, 4, 5, 20]
num.sort()
print(num)

# iterating on a list #for name_of_var in iterable
for x in num:
    print(x)
