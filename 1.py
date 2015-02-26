def method1():
    p = 0
    for i in xrange(1000):
        if i % 3 == 0 or i % 5 == 0:
            p += i
    print p

def method2():
    print sum([x for x in xrange(1000) if x % 3 == 0 or x % 5 == 0])

method2()
