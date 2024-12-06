#set.add(el)
collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(3)

print(collection)


#set.remove(el)
collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(3)

collection.remove(2)
print(collection)


#set.clear(el)
collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(3)

collection.clear()
print(collection)


#set.pop(el)
collection = set()
collection.add(1)
collection.add(1)
collection.add(2)


collection.pop()
print(collection)


#set.union(set1)
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2))
print(set1)
print(set2)



#set.union(set1)
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.intersection(set2))
