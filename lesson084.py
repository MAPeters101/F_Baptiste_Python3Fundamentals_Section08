
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




