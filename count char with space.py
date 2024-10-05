a=input()
b=a.split()
c={}
for i in range(b):
  if b[i] in c:
    c[b[i]] += 1
  else:
    c[b[i]] = 1
print(c)
