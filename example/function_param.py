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

# 命名关键字参数
def person_kw(name, age, *, city='houston', job):
    print(name, age, city, job)

person_kw('bird', '58', city='boston', job='manager')
person_kw('paul', '35', job = '123')

# 参数顺序
def param_index(a, b=0, *c, d, **e):
    print(a, b, c, d, e)
param_index(1, 2, 'a', 'b', d=3, e=4, g=5)
args=(1,2,3,4)
kw={'d':9, 'x': '#'}
param_index(*args, **kw)

# exercise
# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
# def product(x, y):
#     return x * y

def product(*y):
    if y is None:
        raise TypeError('param is none')
    elif len(y) == 0:
        raise TypeError('param is empty')
    else:
        mul = 1
        for num in y:
            mul = mul * num
        return mul

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')



