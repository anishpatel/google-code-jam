
FILE_NAME = '10_finals_A'

inpt = open('{0}.in'.format(FILE_NAME), 'r')
out = open('{0}.out'.format(FILE_NAME), 'w')
log = open('{0}.log'.format(FILE_NAME), 'w')

def print_case(case_num, result):
    out.write('Case #{0}: {1}\n'.format(case_num, result))

def check_palindrome(seq, i, j):
    if i == j:
        return True
    elif seq[i] == seq[j]:
        check_palindrome(seq, i+1, j-1)
    else:
        return False

num_cases = int(inpt.readline()[:-1])
for case_num in xrange(1, num_cases+1):
    s = inpt.readline()[:-1]
    # consider printing all elements
    counter = len(s)
    # replace sequence of repeated elements 
    s = reduce(lambda seq, ltr: ''.join(seq, ltr) if seq[-1] != ltr else seq, s)
    # find any palindrones
    s_len = len(s)
    new_s = s
    for i in xrange(0, s_len, 2):
        for j in xrange(i, s_len, 2):
            if check_palindrome(s, i, j):
                counter += (j - i) * 2
                new_s = s[i:] + s[j+1:]
    
    print_case(case_num, counter)

inpt.close()
out.close()
log.close()
print 'done.'

num_cases = 4
with open('{0}.out'.format(FILE_NAME), 'r') as out:
    print '{0}.out:'.format(FILE_NAME)
    for case_num in xrange(num_cases):
        print out.readline(),
