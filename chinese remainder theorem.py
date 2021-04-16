def ext_gcd(a,b):
    if b==0:return (a,1,0)
    g,c,d=ext_gcd(b, a%b)
    return (g,d,c-(a//b)*d)


# crt(a,mod1,c,mod2) return t
def crt(a,mod1,c,mod2):
    g,p,q = ext_gcd(mod1,mod2)
    if abs(c-a)%g != 0:return -1
    s = abs(a-c)//g
    t = mod1*p*s+a
    lcm = mod1*mod2//g
    return t%lcm