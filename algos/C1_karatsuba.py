def karatsuba(int1,int2):
    """multiples two integers together using karatsubas integer multiplication algorithm
    recursive algorithm
    assume the integers are of length which is a power of 2

    Args:
        int1 (int): same length as int2
        int2 (int): same length as int1

    Returns:
        int: 
    """

    if len(str(int1)) ==1 or len(str(int2))==1 :
        return int1*int2
    n = max(len(str(int1)),len(str(int2)))
    nby2=n//2

    a = int1 // 10**(nby2)
    b = int1 % 10**(nby2)
    c = int2 // 10**(nby2)
    d = int2 % 10**(nby2)

    p = a+b
    q = c+d
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)

    return 10**(2*nby2)*ac+10**(nby2)*(karatsuba(p,q)-ac-bd)+bd


def testing(int1,int2):
    n = max(len(str(int1)),len(str(int2)))
    nby2=n//2

    a = int1 // 10**(nby2)
    b = int1 % 10**(nby2)
    c = int2 // 10**(nby2)
    d = int1 % 10**(nby2)

    print(int1,int2)
    print(a,b,c,d)

# testing(6327,5297)
# testing(65,195)
# testing(5456,5921458)


print(6327*5297)
print(karatsuba(6327,5297))