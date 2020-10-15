def lcm(x, y):
    lcm = (x*y)//gcd(x, y)
    return lcm

def gcd(b, c): 
  
   while(c): 
       b, c = c, b % c 
  
   return b

def rel(v):
    total = 0
    for a in range(1, v + 1):
        if gcd(a, v) == 1:
            total = total + 1
    return total

def listofdiv(v):
    listofdiv = [k for k in range(1, v + 1) if not v % k]
    return listofdiv

def elcountlist(v1, v2, v3):
    listofcases = []
    list1 = listofdiv(v1)
    list2 = listofdiv(v2)
    for s in list1:
        for t in list2:
            if lcm(s,t) == v3:
                listofcases.append((rel(s)*rel(t)))
    return listofcases

def elpairs(v1, v2, v3):
    listofcases = []
    list1  = listofdiv(v1)
    list2 = listofdiv(v2)
    for s in list1:
        for t in list2:
            if lcm(s,t) == v3:
                listofcases.append((s,t))
    return listofcases

def elcount(v1, v2, v3):
    list1 = elcountlist(v1, v2, v3)
    total = 0
    for l in list1:
        sum(list1)
        total = sum(list1) 
    return total

def cycsubcount(v1, v2, v3):
    total  =  elcount(v1, v2, v3)//rel(v3)
    return total

print(elpairs(56,7,8))