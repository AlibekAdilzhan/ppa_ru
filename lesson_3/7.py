from itertools import product


a = ["".join(x) for x in product("12", repeat=5)]
print(len(set([x for x in a if "12" in x])))
# print(set([x for x in a if "12" in x]))

