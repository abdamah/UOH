# Chapter 2: Data Structures

# list: is an ordered collection of items is mutable

mylist = [1, 2, 3, 4, 5]
print("original: ", mylist)
print("id:", id(mylist))
mylist.append(6)  # append adds an item to the end
print("id:", id(mylist))
print("append:", mylist)
mylist.insert(2, 7)  # insert adds an item at a given index
print("id:", id(mylist))
print("insert:", mylist)
mylist.remove(3)  # remove removes the first occurrence of a value
print("id:", id(mylist))
print("remove:", mylist)
mylist.pop()  # pop removes the last item
print("id:", id(mylist))
print("pop:", mylist)
mylist.sort()  # sort sorts the list in place
print("id:", id(mylist))
print("sort:", mylist)
mylist.reverse()  # reverse reverses the list in place
print("reverse:", mylist)

# tuple: is an ordered collection of items is immutable
mytuple = (1, 2, 3, 4, 5)
print("\nTuple:")
print("original: ", mytuple)
print("id:", id(mytuple))
# count returns the number of occurrences of a value
print("count:", mytuple.count(1))
# index returns the index of the first occurrence of a value
print("index:", mytuple.index(1))
print("id:", id(mytuple))
print("slice:", mytuple[1:3])  # slice returns a slice of

mytuple = (1, 2, 3, 4, 5)

# Adding 6 directly to a tuple (not possible, tuples are immutable)
mytuple += (6,)  # This works because it creates a new tuple by concatenation
print("modified:", mytuple)
print("id:", id(mytuple))

# Removing 3 directly from a tuple (not possible, will raise an error)
# mytuple.remove(3)  # ERROR: 'tuple' object has no attribute 'remove'

# Set: is an unordered collection of unique items
myset = {1, 2, 3, 4, 5}
print("\nSet:")
print("original: ", myset)
print("id:", id(myset))
print("add:", myset.add(6))  # add adds an item to the set
print("id:", id(myset))
print("add:", myset)
print("remove:", myset.remove(3))  # remove removes an item from the set
print("id:", id(myset))
print("discard:", myset.discard(3))  # discard removes an item from the set
print("id:", id(myset))
# pop removes and returns an arbitrary item from the set
print("pop:", myset.pop())
print("id:", id(myset))
print("clear:", myset.clear())
print("original:", myset)  # clear removes all items from the set

# Dictionary: is an ordered collection of key-value pairs
mydict = {
    "name": "Abdallah",
    "age": 25,
    "title": "Developer"
}
print("\nDictionary:")
print("original: ", mydict)
print("id:", id(mydict))
print("get:", mydict.get("name"))  # get returns the value for a given key
print("id:", id(mydict))
# keys returns a view of the keys in the dictionary
print("keys:", mydict.keys())
print("id:", id(mydict))
# values returns a view of the values in the dictionary
print("values:", mydict.values())
print("id:", id(mydict))
# items returns a view of the key-value pairs in the dictionary
print("items:", mydict.items())
print("id:", id(mydict))
# update updates the value for a given key
print("update:", mydict.update({"age": 26}))
print("id:", id(mydict))
print("update:", mydict)
print("id:", id(mydict))
# pop removes a key-value pair from the dictionary
print("pop:", mydict.pop("age"))
print("id:", id(mydict))
print("pop:", mydict)
print("id:", id(mydict))
# popitem removes and returns the last inserted key-value pair
print("popitem:", mydict.popitem())
print("id:", id(mydict))
print("popitem:", mydict)
print("id:", id(mydict))
# clear removes all key-value pairs from the dictionary
print("clear:", mydict.clear())
print("original:", mydict)  # clear removes all items from the dictionary
