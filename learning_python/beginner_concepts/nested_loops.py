# nested loops = The inner loop finishes all of its iterations before finishing one iteration for the outer loop

rows = int(input("Enter the amount of rows: "))
columns = int(input("Enter the amount of columns: "))
symbol = input("Enter a symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
