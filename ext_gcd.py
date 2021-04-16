def ext_gcd(a,b):
    if b==0:return (a,1,0)
    g,c,d=ext_gcd(b, a%b)
    return (g,d,c-(a//b)*d)
