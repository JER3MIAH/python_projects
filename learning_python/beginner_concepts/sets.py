# a set is a collection which is unordered and has no index. No duplicates

powers = {"super strength", "lasers", "flight"}
abilities = {"speed", "toughness", "endurance", "flight"}

powers.add("fire breath")  # adds an item to the set
powers.remove("lasers")  # I lost my laser powers :(
powers.update(abilities)  # this adds the update set to my powers set
awakening = powers.union(abilities)  # combines both sets using a different variable

print(awakening)

print()  # newline

print(powers.difference(abilities))  # what does powers have that abilities doesn't have in the set?

print()  # newline

print(powers.intersection(abilities))  # checks what both sets have in common

print()  # newline

for i in powers:  # the order at which this is printed is random
    print(i, end=" ")
