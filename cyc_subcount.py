
def lcm(x, y):
    """lcm returns the leat common multiple of two inputs."""
    return (x*y) // gcd(x, y)


def gcd(b, c):
    """gcd returns the greatest common division of two inputs."""
    while c:
        b, c = c, b % c
    return b


def rel(v):
    """
    rel goes through the defined range and finds the values that have gcd(v,k) = 1, then returns a count of those values
    for more information about this search the term Euler totient function.
    """
    total = 0
    for a in range(1, v + 1):
        if gcd(a, v) == 1:
            total = total + 1
    return total


def listofdiv(v):
    """takes in an input and lists all of its divisors to include itself in a bracketed list"""
    return [k for k in range(1, v + 1) if not v % k]

#v1 = order of first group, v2 = order of second group, and v3 = order of the subgroups you're attempting to count.

#elcountlist calls listofdiv for three and searches for pairs of numbers in the divisors of v1 and v2 which produce lcm = v3.
#elcountlist then calls rel on each number in a pair and multiplies them.
#These values are then added to a bracketed list (e.g. [((rel(1)*rel(5)), (rel(5)*rel(1)), (rel(5)*rel(5))]

def elcountlist(v1, v2, v3):
    listofcases = []
    list1 = listofdiv(v1)
    list2 = listofdiv(v2)
    for s in list1:
        for t in list2:
            if lcm(s, t) == v3:
                listofcases.append((rel(s)*rel(t)))
    return listofcases

#elpairs is not really necessary but is a good way to make sure elcountlist is working properly.
#it simply takes in yourthree inputs and returns the pairs in the divisors that return lcm = v3.
#(e.g. [(1, 5), (5, 1), (5, 5)])

def elpairs(v1, v2, v3):
    listofcases = []
    list1  = listofdiv(v1)
    list2 = listofdiv(v2)
    for s in list1:
        for t in list2:
            if lcm(s,t) == v3:
                listofcases.append((s,t))
    return listofcases

#elcount adds the elements of the list returned by elcountlist together
#(e.g. (rel(1)*rel(5))+(rel(5)*rel(1))+(rel(5)*rel(5)))

def elcount(v1, v2, v3):
    list1 = elcountlist(v1, v2, v3)
    return sum(list1)

#cycsubcount calls both elcount and rel and divides the former by the latter to give you the number of cyclic subgroups.

def cycsubcount(v1, v2, v3):
    total  =  elcount(v1, v2, v3) // rel(v3)
    return total

#the following are test prints to show you what everything will give you when evaluated individually

print(listofdiv(100))

print(listofdiv(25))

print(elpairs(100,25,10))

print(elcountlist(100,25,10))

print(elcount(100,25,10))

print(rel(10))

print(cycsubcount(100,25,10))
