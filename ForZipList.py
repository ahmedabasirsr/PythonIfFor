

l = [1,2,3,4,5]
m = ["n","b","c","x","y"]
n= [7,8,9,4,5]

#  for i in range(len(t1)) and for j in range(len(t2)):
# for i, j in itertools.product(range(x), range(y)):
# for f, b in zip(foo, bar):
for i,j,k in zip(l,m,n):
    print(i,j,k)