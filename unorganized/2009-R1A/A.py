
FILE_NAME = 'A-sample'

unhappies = []

def change_base(num, base):
    ls = []
    while num > 0:
        ls.append(num%base)
        num /= base
    ls.reverse()
    return int(''.join(str(i) for i in ls))

def func(n, base):
    n = change_base(n, base)
    #raw_input(str(n))
    if n == 1:
        return True
    elif n in unhappies:
        return False
    else:
        unhappies.append(n)
        return func(sum(int(digit)**2 for digit in str(n)), base)

def do_case(bases):
    try:
        bases = list(bases)
        counter = 2
        while True:
            for base in bases:
                print '___', counter, base
                b = func(counter, base)
                print b
                if not b:
                    break
            else:
                return counter
            counter += 1
    except:
        print counter, base
        raise

with open('{0}.in'.format(FILE_NAME), 'r') as inpt:
    with open('{0}.out'.format(FILE_NAME), 'w') as out:
        T = int(inpt.readline()[:-1])
        for t in xrange(1, T+1):
            print '___________', t
            data = (int(value) for value in inpt.readline()[:-1].split(' '))
            result = do_case(data)
            out.write('Case #{0}: {1}\n'.format(t, result))

print 'done.'
