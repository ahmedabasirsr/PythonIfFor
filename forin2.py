for i in range(2,6,1):
    print(i)
# for here works form 2 to 6 with by one step(4 values)

print("*************************")

# for here works from 0 to 5 but its break where i=3 (3 values)
for i in range(6):
    if i == 3:
        break
    print(i)

print("*************************")

# for here works from 0 to 6 but exept value  i =3 (5 values)
for i in range(6):
    if i == 3:
        continue
    print(i)
