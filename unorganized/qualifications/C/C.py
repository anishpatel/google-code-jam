from math import factorial

FILE_NAME = 'A-small-sample'

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
    N = int(inpt.readline()[:-1])
    sean_vals = []
    candies = [int(i) for i in inpt.readline()[:-1].split(' ')]
    
    
    
    print_case(t, max(sean_vals) if sean_vals else 'NO')    

inpt.close()
out.close()
print 'done.'

num_cases = 2
with open('{0}.out'.format(FILE_NAME), 'r') as out:
    print '{0}.out:'.format(FILE_NAME)
    for case_num in xrange(num_cases):
        print out.readline(),
