# Extended and ordinary Euclidean algorithms
def eeuclid(x,y):
    """
    d,r,s = eeuclid(x,y)
    Returns d = gcd(x,y) and r, s where r*x+s*y == d.
    All inputs and outputs are integers; x, y >= 0
    """
    if x == 0:
        return (y, 0, 1)
    if y == 0:
        return (x, 1, 0)
    q = x // y
    d,r1,s1 = eeuclid(y, x-y*q)
    # d == r1*y+s1*(x-y*q) == s1*x +(r1-q*s1)*y
    r, s = s1, r1-q*s1
    return (d, r, s)

def gcd(x,y):
    """
    d = gcd(x,y)
    Uses standard Euclidean algorithm to compute gcd(x,y)
    Assumes all inputs non-negative integers
    """
    if x == 0:
        return y
    if y == 0:
        return x
    q = x // y
    return gcd(y, x-y*q)

if __name__ == "__main__":
    print(eeuclid(57,21))
