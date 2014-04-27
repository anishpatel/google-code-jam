#FILE_NAME = 'B-sample'
#FILE_NAME = 'B-small-attempt2'
FILE_NAME = 'B-large'

def func(line):
    data = parse(line)
    data.next() # unneeded
    nSurprisers = data.next()
    p = data.next()
    scores = sorted(data, reverse=True)
    
    i = 0
    temp1 = p*3 - 2
    while (i < len(scores)) and (scores[i] >= temp1): i += 1
    scores1 = scores[:i]
    j = i
    temp2 = temp1 - 2
    if temp2 < 2: temp2 = 2
    while (j < len(scores)) and (scores[j] >= temp2): j += 1
    scores2 = scores[i:j]

    l = len(scores2)
    if l > nSurprisers: l = nSurprisers
    
    return len(scores1) + l

parse = lambda s: (int(item) if item.isdigit() else item.upper() for item in s.split())
with open('{}.in'.format(FILE_NAME), 'r') as fin:
    with open('{}.out'.format(FILE_NAME), 'w') as fout:
        readln = lambda: fin.readline().strip()
        nCases = int(readln())
        for case in xrange(1, nCases+1):
            result = func(readln())
            fout.write('Case #{}: {}\n'.format(case, result))
