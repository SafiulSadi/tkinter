def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

x = add(3,4,1,5,1,1)
print(x)