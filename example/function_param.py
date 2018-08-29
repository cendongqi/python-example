# 位置参数
# def power(x):
#     return x * x

# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2, 3))

print(power(2))

# 默认参数的坑
def add_end(L=[]):
    L.append('END')
    return L
add_end()
add_end()
add_end()
add_end()
print(add_end())

# 解决坑的方案，最好使用不可变对象
def add_end_1(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

add_end_1()
add_end_1()
add_end_1()
add_end_1()
add_end_1()
add_end_1()
add_end_1()
print(add_end_1())


# 可变参数
def calc(numbers):
    sum = 0
    for num in numbers:
        sum = sum + num * num
    return sum
print(calc((1,2,3,4,5,6,7,8)))
print(calc([1,2,3,4,5,6,7,8]))


def calc_1(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num * num
    numbers = []
    print('numbers',numbers)
    return sum

print(calc_1(1,2,3,4,5,6,7,8,9,10))

nums = [4,5,123,4,51,23]
print(calc_1(*nums))
print('old_nums',nums)

# 关键字参数
def person(name, age, **kw):
    print('name:,', name, 'age:,', age, 'other:', kw)

person('williams', 30)
person('cury', 31, city='orando', team='Golden Warriors')

infos = {'city':'houston','teamname':'rocket'}
person('yao', 32, **infos)


