d = {
    'key 1': 1,
    'key 2': 2,
    3.14: 'pi'
}

for k in d:
    print(k)

for k in d:
    print(f'd[{k}] = {d[k]}')
print()

for k in d:
    print(d[k])
print()

for v in d.values():
    print(v)
print()

for t in d.items():
    print(t)
print()


