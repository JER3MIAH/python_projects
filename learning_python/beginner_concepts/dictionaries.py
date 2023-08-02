#  a dictionary is a changeable, unordered, collection of unique key value pairs
#   They are fast because they use hashing. They allow us to access a value quickly

capitals = {'USA': 'washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

capitals.update({'Germany': 'Berlin'})  # adds a new key and value to the dictionary.
#                                         You can also use it to update existing key:values
capitals.pop('China')  # removes a key value
# capitals.clear()  # clears the entire dictionary
# print(capitals['China'])  # prints the value assigned to the key entered. *unsafe*
print(capitals.get('Nigeria'))  # safer way to do the above, avoiding errors if the key does not exist
print(capitals.keys())  # this prints all the keys
print(capitals.values())  # this prints all the values
print(capitals.items())  # this prints out both the keys and the values

for key, value in capitals.items():  # this iterates once for each key: value, essentially printing out all the items
    print(key, value)
