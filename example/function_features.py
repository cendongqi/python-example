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
for k,v in d.items():
    print(k, '--', v)

from collections import Iterable

print(isinstance('src', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

for index, value in enumerate((1,2,4,5,6,7,8,9)):
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
print(min_and_max([8,7,6,5,4,3,2,1]))
