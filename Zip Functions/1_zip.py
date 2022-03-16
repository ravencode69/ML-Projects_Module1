# takes corrosponding element and glue them together
list1 = [1, 2, 3, 4, 5]
list2 = ['one', 'two', 'three', 'four']

zip1 = list(zip(list1, list2))

print(zip1)
# [(1, 'two'), (2, 'three'), (3, 'four'), (4, 'one')

unzip = list(zip(*zip1))
print(unzip)

items = ['apple', 'banana', 'orange']
count = [3, 6, 5]
pr = [0.99, 0.23, 0.43]

sentences = []
for(item, count, pr) in zip(items, count, pr):
    item, count, pr = str(item), str(count), str(pr)
    sen1 = 'I bought '+count+' '+item+'s for '+pr+' .'
    sentences.append(sen1)
print(sentences)
