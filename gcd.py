#Maior divisor comum entre A e B
def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
