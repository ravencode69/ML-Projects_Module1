# list with constraints-->tuple()
t = (1, 2, 3)
print(t[0])
# you can't add or remove elements from it : stable structured kind of data type

credit_card = (123456789, "raven", '23/23', 123)
credit_card2 = (123456789, "raven", '23/23', 123)

credit_cards = [credit_card, credit_card2]

print(credit_cards)

# unpacking a tuple
person1 = ("nancy drew", 25, "coke")
person2 = ("joe cook", 23, "tako")

persons = [person1, person2]

for name, age, food in persons:
    print(age)
    print(name)
    print(food)
