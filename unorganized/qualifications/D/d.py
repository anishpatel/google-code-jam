from math import factorial

FILE_NAME = 'D-large'

inpt = open('{0}.in'.format(FILE_NAME), 'r')
out = open('{0}.out'.format(FILE_NAME), 'w')
def print_case(case_num, result):
    out.write('Case #{0}: {1:f}\n'.format(case_num, result))

def find_loop(array, indices):
    cur_i = indices[-1]
    cur_e = array[cur_i-1]
    nxt_e = array[cur_e-1]
    indices.append(cur_e)
    if indices[0] == nxt_e:
        return
    else:
        find_loop(array, indices)

num_cases = int(inpt.readline()[:-1])
for case_num in xrange(1, num_cases+1):
    N = int(inpt.readline()[:-1])
    hits = 0.
    array = [int(i) for i in inpt.readline()[:-1].split(' ')]
    chked_indices = [i for index, i in enumerate(array) if i-1 == index]
    for n in xrange(1, N+1):
        if n in chked_indices:
            chked_indices.remove(n)
            continue
        indices = [n]
        find_loop(array, indices)
        hits += factorial(len(indices)) / factorial(len(indices)-1)    
        chked_indices.extend(i for i in indices if i > n)
    print_case(case_num, hits)    

inpt.close()
out.close()
print 'done.'

num_cases = 3
with open('{0}.out'.format(FILE_NAME), 'r') as out:
    print '{0}.out:'.format(FILE_NAME)
    for case_num in xrange(num_cases):
        print out.readline(),
