
data = {
    'open': 100,
    'high': 110,
    'low': 95,
    'close': 110,
}

print('open' in data)
print(3.14 in data)
print('open' not in data)
print('x' not in data)
print()

l = [1,2,3,4]
print(3 in l)
print(10 not in l)
print()

data.clear()
print(data)
print(len(data))

data = {
    'open': 100,
    'high': 110,
    'low': 95,
    'close': 110,
}
print(data)
print(len(data))
print('-'*80)


data_copy = data.copy()
print(data)
print(data_copy)
print(data is data_copy)
data_copy['x'] = 100
print(data)
print(data_copy)
print('-'*80)

from copy import deepcopy
data_copy = deepcopy(data)
print(data)
print(data_copy)
print(data is data_copy)
print('-'*80)


d = {
    'a': [1,2,3],
    'b': {
        'x': 0,
        'y': 0
    }
}

d_copy = d.copy()
print(d_copy is d)
d['b'] = 100
print(d)
print(d_copy)
print('-'*40)

d = {
    'a': [1,2,3],
    'b': {
        'x': 0,
        'y': 0
    }
}
d_copy = d.copy()
print(d_copy is d)
print(d)
print(d_copy)
d['a'].append(4)
print(d)
print(d_copy)
print('-'*40)


d = {
    'a': [1,2,3,4],
    'b': {
        'x': 0,
        'y': 0
    }
}
d_copy = deepcopy(d)
print(d_copy is d)
print(d)
print(d_copy)
d_copy['a'].append(5)
print(d)
print(d_copy)
print('-'*80)

d = dict(a=1, b=2)
print(d)
d= {3.14: 'pi', 2: 'even'}
print(d)
#d = dict(2='even')

