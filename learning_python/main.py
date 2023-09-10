# list comprehension

my_list = [num ** 2 for num in range(0, 100)]
my_list2 = [(num ** 2) for num in range(0, 100) if num % 2 == 0]

print(my_list2)
