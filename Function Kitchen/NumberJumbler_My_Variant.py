import random


def NJumbler(N):  # (whole number range end)

    assign = []
    while len(assign) < N+1:
        y = random.randint(0, N)
        if y in assign:
            pass
        else:
            assign.append(y)

    Jumbled = {}
    for x in range(0, N+1):
        Jumbled.update({str(x): str(assign[x])})

    return(Jumbled)


"""
olist = ['+', '-', '/', '*, ' **']
solist = random.sample(olist)
"""

x = NJumbler(10)
print(x)
