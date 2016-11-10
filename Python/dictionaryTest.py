phonebook = {'a':'1111','b':'2222'}
print(phonebook)
d = dict(name ='a',age = 25)
print(d['name'])
print(d)
print(len(d))
print('age' in d)
x = {}
x[30] = 'aaaa'
print(x)
people = {
	'Alice':{
		'phone':'12345',
		'address':'asdasd'
	},
	'Tom':{
		'phone':'12345',
		'address':'asdasd'
	},
	'Jerrey':{
		'phone':'12345',
		'address':'aaaaaa'
	}
}
labels = {
	'phone':'phone number',
	'addr':'address'
}
name = raw_input('name:')
request = raw_input('phone or address?')
if request == 'p':key = 'phone'
if request == 'a':key = 'address'
if name in people:print("%s's %s is %s")%(name,key,people[name][key])
















