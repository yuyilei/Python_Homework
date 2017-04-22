L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

L1 = sorted(L, key=lambda t:str.lower(t[0]))
print(L1)

L2 = sorted(L, key=lambda t:t[1],reverse=True)
print(L2)
