l1 = [-4, 5, 1, 0, -6, -19, 24, 44, 69, 9, -15]
l2 = [i for i in l1 if i > 0]
print(l2)

l3 = sum([i for i in l1 if i < 0])
print(l3)

x = ['ab', "ba"]
for j in x:
    print(j.upper())

for i in x:
    i.upper()
    print(x)

