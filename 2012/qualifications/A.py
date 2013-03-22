#FILE_NAME = 'A-sample'
FILE_NAME = 'A-small-attempt0'

mapping = [24, 7, 4, 18, 14, 2, 21, 23, 3, 20, 8, 6, 11, 1, 10, 17, 25, 19, 13, 22, 9, 15, 5, 12, 0, 16]

def func(line):
    return ''.join(c if c == ' ' else chr(mapping[ord(c)-97]+97) for c in line)

with open('{}.in'.format(FILE_NAME), 'r') as fin:
    with open('{}.out'.format(FILE_NAME), 'w') as fout:
        readln = lambda: fin.readline().strip()
        nCases = int(readln())
        for case in xrange(1, nCases+1):
            result = func(readln())
            fout.write('Case #{}: {}\n'.format(case, result))
