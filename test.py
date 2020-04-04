dictest = {
    '1': 'one',
    '2': 'two',
    '3': 'three'
}

k = list(dictest.keys())
v = list(dictest.values())
dictest.clear()

for i in range(0, len(k)):
    k[i] = int(k[i])

for i in range(0, len(k)):
    dictest.update({k[i]: v[i]})

print(dictest)
