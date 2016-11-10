format = "hello. %s.%s enough for ya"
value = ('world','hot')
print format%value

s = 'asdsfdasafas'.find('a',2,4) 

print(s)

dirs = 'a','b','c','d'
a = '/'.join(dirs)
b = a.split('/')
print(a)
print(b)
names = ['a','b','c']
name = 'a '
if name.strip() in names : print('find it')
from string import maketrans
table = maketrans('cs','kz')
c = len(table)
print(c)
d = 'this is a incredible test'.translate(table,' ')
print(d)