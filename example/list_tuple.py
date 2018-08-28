classmate = ['Mike', 'John', 'Rose']

# 取值
print(classmate)
print(len(classmate))
print(classmate[0])
print(classmate[1])
print(classmate[2])
print(classmate[-1])
print(classmate[-2])
print(classmate[-3])

print('----------')

# 末尾追加
classmate.append('adam')
print(classmate)

# 插入
classmate.insert(2,'Jack')
print(classmate)

# 末尾删除
classmate.pop()
print(classmate)

# 指定位置删除
classmate.pop(2)
print(classmate)

# 替换
classmate[1] = 'Sarah'
print(classmate)

# 不同类型
exts = [1, 'John', True]
print(exts)

# list嵌套
classmate.append(exts)
print(classmate)

# 空list
emptyList = []
print(len(emptyList))

# tuple
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

# 空tuple
p = ()
print(len(p))

# 一个元素的tuple
t = (1)
print(t)
t = (1,)
print(t)

# exercise
# 请用索引取出下面list的指定元素：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])




