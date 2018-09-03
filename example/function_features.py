# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[0:3])
print(L[:3])
print(L[-2:-1])
print(L[-2:])

L = list(range(100))
print(L[:10:2])
print(L[::5])
print(L[:])

T = (1, 2, 4, 5, 6, 7, 8, 9)
print(T[:])
print('ABCDEFG'[0:2])


# exercise
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    return s


# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for n in d:
    print(n)
for value in d.values():
    print(value)
for k, v in d.items():
    print(k, '--', v)

from collections import Iterable

print(isinstance('src', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

for index, value in enumerate((1, 2, 4, 5, 6, 7, 8, 9)):
    print('index:', index, ',value:', value)


# exercise
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def min_and_max(t):
    if not isinstance(t, (list)):
        raise TypeError('param not list')
    min = t[0]
    max = t[0]
    for n in t:
        if min > n:
            min = n
        if max < n:
            max = n
    return min, max


print(min_and_max([8, 7, 6, 5, 4, 3, 2, 1]))

# 列表生成式
print('---------------列表生成式---------------')
print(list(range(1, 11)))
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

print([x * x for x in (range(1, 11))])
print([x for x in range(101) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

import os

print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# exercise
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
# L = ['Hello', 'World', 18, 'Apple', None]

# >>> [s.lower() for s in L]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <listcomp>
# AttributeError: 'int' object has no attribute 'lower'

# 使用内建的isinstance函数可以判断一个变量是不是字符串：
# >>> x = 'abc'
# >>> y = 123
# >>> isinstance(x, str)
# True
# >>> isinstance(y, str)
# False

# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [str.lower() for str in L1 if not isinstance(str, (int, float)) and str is not None]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


# 生成器
print('---------------生成器---------------')
print([x * x for x in range(1, 100)])
print((x * x for x in range(1, 100)))
g = (x for x in range(101))
for n in g:
    print(n)

# 斐波那契数列 除第一个数和第二数外，任意一个数都可以由前两个数相加得到
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)

def fib_genertor(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib_genertor(6))

for n in fib_genertor(6):
    print(n)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
o = odd()
print(next(o))
print(next(o))
print(next(o))


b = fib_genertor(8)
while True:
    try:
        x = next(b)
        print('x =', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 迭代器

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance(100, Iterable))

from collections import Iterator

print('---------分割线')
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance(100, Iterator))
print(isinstance((x * x for x in range(10)), Iterator))


