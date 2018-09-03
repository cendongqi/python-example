def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

r = range(1, 10)
def f(x):
    return x * x
print(list(map(f, r)))

print(list(map(str, [1,2,3,4,5,6,7,8])))