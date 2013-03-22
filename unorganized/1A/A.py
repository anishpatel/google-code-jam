from fractions import Fraction

FILE_NAME = 'A-large'

def do_case(data):
    N, Pd, Pg = data
    denom = Fraction(Pd, 100).denominator
    n = denom
    while n < N+1:
        if Pg == 100 and Pd != 100:
            n+= denom
            continue
        if Pg == 0 and Pd != 0:
            n += denom
            continue
        return True        
    return False

with open('{0}.in'.format(FILE_NAME), 'r') as inpt:
    with open('{0}.out'.format(FILE_NAME), 'w') as out:
        T = int(inpt.readline()[:-1])
        for t in xrange(1, T+1):
            data = (int(value) for value in inpt.readline()[:-1].split())
            result = do_case(data)
            out.write('Case #{0}: {1}\n'.format(t, 'Possible' if result else 'Broken'))

print 'done.'
