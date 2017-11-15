print "hello python"

g = (x for x in range(10))

for x in g:
    print x


def fil(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n+1

print "----------------------"
g2 = fil(10)

for f in fil(10):
    print f

def mapfu(x):
    return "INFO-"+str(x)

l = [0,1,2,3,4,5,6,7,8,9]
lm = map(mapfu ,l)
print lm
print l