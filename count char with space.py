a=input()
b=a.split()
d=str(b)
c={}
  
for i in range(len(b)):
  if b[i].isdigit():
      print("ivalidinput")
      c={}
      break
  elif b[i] in c:
      c[b[i]] += 1
  else:
      c[b[i]] = 1
for i in c:
    print(i ,c[i],end = " ")

