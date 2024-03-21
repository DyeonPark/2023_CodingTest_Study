selfnum = set([i for i in range(1, 10000)])
i=1
while i<=10000:
    d_i = i + sum(list(map(int, list(str(i)))))
    selfnum.discard(d_i)
    i+=1
for s in selfnum: print(s)