from itertools import combinations

FILE_NAME = 'B-sample'
#FILE_NAME = 'B-small-attempt0'
#FILE_NAME = 'B-large'
#FILE_NAME = 'B-practice'

def chk_validity(points):
    for p in points:
        if points[p] != 1:
            return False
    for p1, p2 in combinations(points.iterkeys

def do_case():
    num_points, min_dist = get_ints()
    points = dict()
    for i in xrange(num_points):
        point, num_vendors = get_ints()
        points[point] = num_vendors
    

with open('{0}.in'.format(FILE_NAME), 'r') as inpt:
    with open('{0}.out'.format(FILE_NAME), 'w') as out:
        get_line = lambda: inpt.readline()[:-1]
        get_int = lambda: int(get_line())
        get_split = lambda: get_line().split()
        get_ints = lambda: int(i) for i in get_split()
        T = get_int()
        for t in xrange(1, T+1):
            result = do_case()
            out.write('Case #{0}: {1}\n'.format(t, result))

print 'done.'
