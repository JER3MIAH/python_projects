# filter() =    creates a collection of elements from an iterable,
#               for which a function returns true
#
#               filter(function, iterable)

friends = [("Jeremiah", 20),
           ("Ololade", 18),
           ("Blade", 17),
           ("James", 16),
           ("Henry", 28),
           ("Bones", 25)]

age = lambda data: data[1] >= 18

drinking_buds = list(filter(age, friends))

for i in drinking_buds:
    print(i)