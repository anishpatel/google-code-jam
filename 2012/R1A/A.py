#FILE_NAME = 'B-sample'
#FILE_NAME = 'B-small-attempt2'
FILE_NAME = 'B-large'

def func():
    A, B = parseInt(readln())
    key_probs = list(parseFloat(readln()))

    nKey_combos = 2**A
    for i in xrange(nKey_combos):
        

    nKeys_enter = A + B
    nKeys_cont = 0
    for keyP in key_probs:
        nKeys_cont += 
    
    return prob

parseInt = lambda s: (int(item) if item.isdigit() else item.upper() for item in s.split())
parseFloat = lambda s: (float(item) if item.isdigit() else item.upper() for item in s.split())
with open('{}.in'.format(FILE_NAME), 'r') as fin:
    with open('{}.out'.format(FILE_NAME), 'w') as fout:
        readln = lambda: fin.readline().strip()
        nCases = int(readln())
        for case in xrange(1, nCases+1):
            result = func()
            fout.write('Case #{}: {}\n'.format(case, result))
