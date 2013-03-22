from itertools import izip

with open('08_A1.in', 'r') as inpt:
    with open('08_A1.out', 'w') as out:
        for case in xrange(1, int(inpt.readline()[:-1])+1):
            inpt.readline()
            V1 = sorted((int(i) for i in inpt.readline()[:-1].split(' ')))
            V2 = sorted((int(i) for i in inpt.readline()[:-1].split(' ')), reverse=True)
            out.write('Case #{0}: {1}\n'.format(case, sum((v1*v2 for v1, v2 in izip(V1, V2)))))

print 'done.'
