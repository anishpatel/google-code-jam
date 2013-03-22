
#FILE_NAME = 'B-sample'
#FILE_NAME = 'B-small-attempt2'
#FILE_NAME = 'B-large'
FILE_NAME = 'B-small-practice'

     

def do_case():
    it = get_ints()
    boosters = it.next()
    build_time = it.next()
    N = it.next()
    C = it.next()
    dists = tuple(it.next() for i in xrange(C))
    dist = lambda i: dists[i%C]
    time_passed = 0
    n = 0
    rem_dist = 0
    while time_passed < build_time:
        time_passed += dist(n) * 2
        n += 1
    if time_passed > build_time:
        n -= 1
        rem_dist = .5 * (time_passed-build_time)
        time_passed = build_time#-= dist(n)/.5
    
    stars_left = dict()
    for d in dists:
        stars_left[d] = 0
    if rem_dist != 0:
        if rem_dist == int(rem_dist):
            rem_dist = int(rem_dist)
        stars_left[rem_dist] = 1
    for tmp_n in xrange(n+1, N):
        stars_left[dist(tmp_n)] += 1
    while boosters > 0:
        m = max(stars_left)
        if stars_left[m] <= 0:
            stars_left.pop(m)
            continue
        stars_left[m] -= 1
        boosters -= 1
        time_passed += m
    for star in stars_left:
        time_passed += (star*2) * stars_left[star]

    return time_passed
    

with open('{0}.in'.format(FILE_NAME), 'r') as fin:
    with open('{0}.out'.format(FILE_NAME), 'w') as fout:
        get_line = lambda: fin.readline()[:-1]
        get_int = lambda: int(get_line())
        get_split = lambda: get_line().split()
        get_ints = lambda: (int(i) for i in get_split())
        get_iter = lambda: (item for item in get_split())
        case_out = lambda result='': fout.write('Case #{0}: {1}\n'.format(case, result))
        out = lambda result: fout.write('{0}\n'.format(result))
        num_cases = get_int()
        for case in xrange(1, num_cases+1):
            result = do_case()
            case_out(result)

print 'done.'
