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
print(hash(1))



