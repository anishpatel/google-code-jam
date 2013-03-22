
FILE_NAME = 'B-large-practice'

inpt = open('{0}.in'.format(FILE_NAME), 'r')
out = open('{0}.out'.format(FILE_NAME), 'w')
def print_case(case_num, result):
    out.write('Case #{0}: {1}\n'.format(case_num, result))

def intersect_it(_set, iterable):
    for item in iterable:
        if item in _set:
            return True
    else:
        return False

T = int(inpt.readline()[:-1])
for t in xrange(1, T+1):
    it = (word for word in inpt.readline()[:-1].split(' '))
    combo = {
        'Q': dict(),
        'W': dict(),
        'E': dict(),
        'R': dict(),
        'A': dict(),
        'S': dict(),
        'D': dict(),
        'F': dict(),
        }
    oppose = {
        'Q': set(),
        'W': set(),
        'E': set(),
        'R': set(),
        'A': set(),
        'S': set(),
        'D': set(),
        'F': set(),
        }
    
    C = int(it.next())
    for c in xrange(C):
        s = it.next()
        combo[s[0]][s[1]] = s[2]
        combo[s[1]][s[0]] = s[2]
    
    D = int(it.next())
    for d in xrange(D):
        s = it.next()
        oppose[s[0]].add(s[1])
        oppose[s[1]].add(s[0])
        
    N = int(it.next())
    invoke = it.next()
    
    final = []

    for element in invoke:
        if final:
            # check for combo
            if final[-1] in combo[element]:
                final.append(combo[element][final.pop()])
            # check for opposition
            elif intersect_it(oppose[element], final):
                final = []
            else:
                final.append(element)
        else:
            final.append(element)
    
    print_case(t, str(final).replace("'", ''))

inpt.close()
out.close()
print 'done.'

num_cases = 5
with open('{0}.out'.format(FILE_NAME), 'r') as out:
    print '{0}.out:'.format(FILE_NAME)
    for case_num in xrange(num_cases):
        print out.readline(),
