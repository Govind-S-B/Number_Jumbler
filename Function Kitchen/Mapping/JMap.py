def Jmap(licht):  # Jumbled Mapper
    import random

    Jumbled = random.sample(licht, len(licht))

    Mapping = {}

    for x in range(0, len(licht)):
        Mapping[licht[x]] = Jumbled[x]

    return(Mapping)  # returns a dictionary of given list , mapping to random elements of the same list


""" EXAMPLE
print(Jmap(range(0, 100+1)))
"""

# To acess mapping
"""
Map[key] ----> Value        # Map is the variable
Map.get(Value) ----> Key
"""
