import random

N = 10  # whole number limit

l1 = list(range(0, N+1))
l2 = random.sample(l1, len(l1))
Jumbled = {}

for x in l1:
    Jumbled.update({str(x): str(l2[x])})

print(Jumbled)
