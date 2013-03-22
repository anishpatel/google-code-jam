
FILE_NAME = 'C-sample'
#FILE_NAME = 'C-small-attempt0'
#FILE_NAME = 'C-large'
#FILE_NAME = 'C-practice'



def do_case():
    

with open('{0}.in'.format(FILE_NAME), 'r') as inpt:
    with open('{0}.out'.format(FILE_NAME), 'w') as out:
        get_line = lambda: inpt.readline()[:-1]
        get_int = lambda: int(get_line())
        get_split = lambda: get_line().split()
        get_ints = lambda: int(i) for i in get_split()
        num_cases = get_int()
        for case in xrange(1, num_cases+1):
            result = do_case()
            out.write('Case #{0}: {1}\n'.format(case, result))

print 'done.'
