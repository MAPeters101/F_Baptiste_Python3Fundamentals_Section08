d = {'a':1, 'b':2, 'c':3}
print(d)

person = {
    'first_name': 'Eric',
    'last_name': 'Idle',
    'year_born': 2016
}
print(person['year_born'])
person['year_born'] = 1943
print(person)
print()

person['month_born'] = 'March'
print(person)
print()


d = {3.14: 'pi', 2: 'even', 'prime':7}
print(d)
print(d[3.14])
print(d[2])
print()


l = [1, 2, 3]
#d = {l: 100}
print(hash(100))
print(hash(3.14))
#print(hash(l))
print()

t = (1,2,3,4)
print(hash(t))
t = ([1,2], 3, 4)
#print(hash(t))
print()

d = {
    (0,0): 'origin',
    (1,0): 'unit-x',
    (0,1): 'unit-y'
}
print(d)
print(d[(0,0)])
print('-'*80)

d = {'a':1, 'b':2, 'c':3}
print(d)
print(id(d))
del d['a']
print(d)
print(id(d))
#print(d['x'])
#del d['x']
print('-'*80)


print(globals())
print(type(globals()))
print(globals()['person'])
p = globals()['person']
print(p)
print(p is person)






