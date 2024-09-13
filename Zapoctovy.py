import math

def Find_Squares_Fermat(n):
    a = int(math.sqrt(n)) + 1
    if (a-1)**2 == n:
        return [a-1, 0]
    b = math.sqrt(a**2-n)
    difference = a-b+2
    while True:
        b = math.sqrt(a**2-n)
        if b == int(b):
            return [int(a-b), int(a+b)]
        if difference-(a-b) < 1:
            return ["trial", int(a-b)]
        difference = a-b
        a += 1

def Fermat(n, start):
    l = Find_Squares_Fermat(n)
    if l[1] == 0 and l[0] != "trial":
        return Fermat(l[0], 2) + Fermat(l[0], 2)
    for i in range(start, max(int(n**(1/3))+1, 3)):
        if n%i == 0:
            return [i] + Fermat(n//i, i)
    
        
    
    if l[0] == "trial":
        for i in range(int(n**(1/3))+1, l[1] + 1):
            if n%i == 0:
                return [i] + Fermat(n//i, i)
        return [n]
    else:
        if l[0] == 1:
            return [n]
        else:
            return Fermat(l[0], 2) + Fermat(l[1], 2)

def Fermat_Factorization(n):
    if type(n) != int or n < 1:
        return "error"
    if n == 2 or n == 1:
        return str(n)
    return fact(Fermat(n, 2))

def if_not_sum_of_squares(n):
    return [n]

def Find_Squares_Euler(n):
    a = 1
    test = False
    squares = 0
    while a < math.sqrt(n/2):
        if math.sqrt(n-a**2) == int(math.sqrt(n-a**2)):
            if test:
                return squares + [a, int(math.sqrt(n-a**2))]
            else:
                test = True
                squares = [a, int(math.sqrt(n-a**2))]
        a += 1
                            
def fact(l):
    l.sort()
    s = ""
    p = l[0]
    counter = 0
    for i in l:
        if i == p:
            counter += 1
        else:
            if counter == 1:
                s += " * " + str(p)
            else:
                s += " * " + str(p) + "^" + str(counter)
            counter = 1
            p = i
    if counter == 1:
        s += " * " + str(p)
    else:
        s += " * " + str(p) + "^" + str(counter)
    return s[3:]   
    
        
        
        
def Euler(n):
    if n == 1:
        return []
    if n%2 == 0:
        return [2] + Euler(n//2)
    if n%4 == 3:
        return if_not_sum_of_squares(n)
    if n%4 == 1:
        l = Find_Squares_Euler(n)
        if l == None:
            return if_not_sum_of_squares(n)
        else:
            a = l[0]
            b = l[1]
            c = l[2]
            d = l[3]
            if (a-c)%2 == 1:
                (a, b) = (b, a)
            k = math.gcd(a-c, b-d)
            m = math.gcd(a+c, b+d)
            return Euler(int(k**2/4 + m**2/4)) + Euler(int(((a-c)/k)**2 + ((a+c)/m)**2))
        
def Euler_Factorization(n):
    if n == 1:
        return str(1)
    return fact(Euler(n))

n = int(input("Zadajte cislo: "))

print("Faktorizovanie Eulerovym algoritmom: " + Euler_Factorization(n))
print("Faktorizovanie Fermatovym algoritmom: " + Fermat_Factorization(n))


