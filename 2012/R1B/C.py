FILE_NAME = 'C-sample'
#FILE_NAME = 'C-small-attempt0'
#FILE_NAME = 'C-large'

def bin_search(A, key, l=0, r=-1):
    if r == -1: r = len(A)
    if l == r:
        return A[l] == key
    else:
        mid = (l + r)/2
        if key < A[mid]:
            return bin_search(A, key, l, mid-1)
        elif key > A[mid]:
            return bin_search(A, key, mid+1, r)
        else:
            return True

def func():
    inpt = parseInt(readln())
    N = inpt.next()
    S = list(inpt)
    S.sort(reverse=True)
    print S
    
        
    #for j in J:
    #    fout.write(' ' + str(  100*(2./N-1.*j/X)  ))

parseInt = lambda s: (int(item) if item.isdigit() else item.upper() for item in s.split())
parseFloat = lambda s: (float(item) if item.isdigit() else item.upper() for item in s.split())
with open('{}.in'.format(FILE_NAME), 'r') as fin:
    with open('{}.out'.format(FILE_NAME), 'w') as fout:
        readln = lambda: fin.readline().strip()
        nCases = int(readln())
        for case in xrange(1, nCases+1):
            fout.write('Case #{}:\n'.format(case))
            func()
