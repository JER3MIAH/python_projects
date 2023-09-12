# loop control statements change the execution the loop from its normal sequence
# break: This terminates the loop entirely
# continue: skips to the next iteration of the loop
# pass: does nothing, acts as a placeholder

for i in "123-456-789":
    if i == "-":
        continue
    print(i, end=" ")

print()  # newline

for i in "Jeremiah":
    if i == "e":
        break
    print(i, end="")

print()  # newline

for i in range(1, 21):
    if i == 14:
        pass
    else:
        print(i, end=" ")
