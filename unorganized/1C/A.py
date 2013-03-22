
#FILE_NAME = 'A-sample'
#FILE_NAME = 'A-small-attempt2'
FILE_NAME = 'A-large'
#FILE_NAME = 'A-practice'



def do_case():
    height, width = get_ints()
    pic = []
    for i in xrange(height):
        pic.append([0 if char == '.' else 1 for char in get_line()])

    for rowi in xrange(height-1):
        for coli in xrange(width-1):
            if pic[rowi][coli]==1 and pic[rowi][coli+1]==1 and pic[rowi+1][coli]==1 and pic[rowi+1][coli+1]==1:
                pic[rowi][coli] = 2
                pic[rowi][coli+1] = 3
                pic[rowi+1][coli] = 3
                pic[rowi+1][coli+1] = 2

    for row in pic:
        if 1 in row:
            return False
    else:
        return pic

with open('{0}.in'.format(FILE_NAME), 'r') as inpt:
    with open('{0}.out'.format(FILE_NAME), 'w') as out:
        get_line = lambda: inpt.readline()[:-1]
        get_int = lambda: int(get_line())
        get_split = lambda: get_line().split()
        get_ints = lambda: (int(i) for i in get_split())
        num_cases = get_int()
        for case in xrange(1, num_cases+1):
            result = do_case()
            if not result:
                out.write('Case #{0}:\n{1}\n'.format(case, 'Impossible'))
            else:
                out.write('Case #{0}:\n'.format(case))
                for r in result:
                    for c in r:
                        if c == 0: out.write('.')
                        elif c == 2: out.write('/')
                        elif c == 3: out.write('\\')
                    out.write('\n')

print 'done.'
