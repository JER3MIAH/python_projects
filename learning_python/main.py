def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b

for i in fib(20):
    print(i)        #generator method

# def fib(num):
#     a = 0
#     b = 1
#     result = []
#     for i in range(num):
#         result.append(a)
#         temp = a
#         a = b
#         b = b + temp
#     return result

# print(fib(20))
