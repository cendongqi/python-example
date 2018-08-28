# 绝对值
print(abs(100))
print(abs(-10))
# 最大值
print(max(1, 2, 3, 4, 5))
# 数据类型转换
print(int(12.13))
print(int('12'))
print(float('12.34'))
print(str(12.31))
print(str(100))
print(bool(1))
print(bool(''))
# exersize
# 利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串
s1 = 66
s2 = 100
print(hex(s1))
print(hex(s2))


# 自定义函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad oprand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(1))


# 空函数
def nop():
    pass


# 返回多个值
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)


# exercise
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程的两个解
def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(b, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(c, (int, float)):
        raise TypeError('bad operand type')

    t = b * b - 4 * a * c
    if t >= 0:
        x1 = (-b + math.sqrt(t)) / (2 * a)
        x2 = (-b - math.sqrt(t)) / (2 * a)
        return x1, x2
    else:
        return print('该方程无实数解')

print('-------------------------------')
# 测试
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

