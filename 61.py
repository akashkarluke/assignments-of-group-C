#way1

d = {1:11,2:22,3:33,4:44}
a=set(d.values())
s=0
for i in a:
    s=s+i

print(s)

#way2

d = {1:11,2:22,3:33,4:44}
sum = 0
for i in d.values():
    sum = sum + i

print(sum)