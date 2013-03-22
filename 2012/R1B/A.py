#FILE_NAME = 'A-sample'
FILE_NAME = 'A-small-attempt0'
#FILE_NAME = 'A-large'

def func():
    inpt = parseInt(readln())
    N = inpt.next()
    J = list(inpt)
    X = sum(J)
    out = [0]*N
    isNeg = False
    for i in xrange(N):
        out[i] = 100*(2./N-1.*J[i]/X)
        if out[i] < 0:
            isNeg = True
            break
    if isNeg:
        
    for j in J:
        fout.write(' ' + str(  100*(2./N-1.*j/X)  ))

parseInt = lambda s: (int(item) if item.isdigit() else item.upper() for item in s.split())
parseFloat = lambda s: (float(item) if item.isdigit() else item.upper() for item in s.split())
with open('{}.in'.format(FILE_NAME), 'r') as fin:
    with open('{}.out'.format(FILE_NAME), 'w') as fout:
        readln = lambda: fin.readline().strip()
        nCases = int(readln())
        for case in xrange(1, nCases+1):
            fout.write('Case #{}:'.format(case))
            func()
            fout.write('\n')
