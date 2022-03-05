import re

text = "a address ThisismyStuff45@gmail.com . some random text .  sldjfa gibberish likerharsh2.o@gmail.com"

pattern = re.compile("[a-zA-Z0-9\.\_]+@+[a-zA-Z0-9]+\.+[a-zA-Z]+")

res = pattern.search(text)
res2 = pattern.findall(text)

print(res)
print(res2)
