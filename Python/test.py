

num = list('12345678910')
print(num[-6::2])

print(len(num))
print(min(num))
print(max(num))
num[2] = '250'
del num[2]
s = ''.join(num)
print(s)
print(num.index('1'))
pop_num = num.pop()
print(num)
num.reverse()

print(pop_num)
print(num)
y = sorted(num)
print(num)
print(y)
x = num
print(x)