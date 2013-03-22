from math import factorial

FILE_NAME = 'A-large'

inpt = open('{0}.in'.format(FILE_NAME), 'r')
out = open('{0}.out'.format(FILE_NAME), 'w')
def print_case(case_num, result):
    out.write('Case #{0}: {1}\n'.format(case_num, result))

def pat_sum(nums):
    counter = 0
    _sum = 0
    while nums:
        _sum += 2**counter * (sum(num%2 for num in nums) % 2)
        nums = [num for num in [num/2 for num in nums] if num is not 0]
        counter += 1
    return _sum    

T = int(inpt.readline()[:-1])
for t in xrange(1, T+1):
    it = (int(char) if char.isdigit() else char for char in inpt.readline()[:-1].split(' '))
    N = it.next()
    time = 0
    seq = []
    rbt_seq = {
        'O': [],
        'B': [],
        }
    pos = {
        'O': 1,
        'B': 1,
        }
    for n in xrange(N):
        rbt = it.next()
        btn = it.next()
        seq.append( (rbt, btn) )
        rbt_seq[rbt].append(btn)
    seq.reverse()
    for rbt in rbt_seq:
        rbt_seq[rbt].reverse()

    while seq:
        rbt, btn = seq[-1]
        if pos[rbt] == btn:
            seq.pop()
            rbt_seq[rbt].pop()
        else:
            rbt = None
        if rbt_seq['O'] and rbt != 'O':
            if pos['O'] < rbt_seq['O'][-1]: pos['O'] += 1
            elif pos['O'] > rbt_seq['O'][-1]: pos['O'] -= 1
        if rbt_seq['B'] and rbt != 'B':
            if pos['B'] < rbt_seq['B'][-1]: pos['B'] += 1
            elif pos['B'] > rbt_seq['B'][-1]: pos['B'] -= 1
        time += 1

    print_case(t, time)

inpt.close()
out.close()
print 'done.'

num_cases = 3
with open('{0}.out'.format(FILE_NAME), 'r') as out:
    print '{0}.out:'.format(FILE_NAME)
    for case_num in xrange(num_cases):
        print out.readline(),
