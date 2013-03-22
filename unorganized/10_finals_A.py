
FILE_NAME = '10_finals_A'

inpt = open('{0}.in'.format(FILE_NAME), 'r')
out = open('{0}.out'.format(FILE_NAME), 'w')
log = open('{0}.log'.format(FILE_NAME), 'w')

def print_case(case_num, result):
    out.write('Case #{0}: {1}\n'.format(case_num, result))

num_cases = int(inpt.readline()[:-1])
for case_num in xrange(1, num_cases+1):
    log.write('case{0}\n'.format(case_num))
    stack = []
    counter = 0
    s = inpt.readline()[:-1]
    slen = len(s)
    
    for index, char in enumerate(s):
        if char in stack:
            nxt_diff_char = None
            if len(stack) >= 3 and char == stack[-3]:
                print case_num, 1, index, char
                i_tmp = index
                while i_tmp < slen and s[i_tmp] == char: i_tmp += 1
                if i_tmp != slen:
                    nxt_diff_char = s[i_tmp]#"""
            if len(stack) >= 1 and stack[-1] == nxt_diff_char:
                print case_num, 2, index, char
                ## push ##
                stack.append(char)
                counter += 1
            else:
                while stack[-1] != char:
                    ## pop ##
                    stack.pop()
                    counter += 1
        else:
            ## push ##
            stack.append(char)
            counter += 1
        ## print ##
        counter += 1
        log.write('{0}, {1}, {2}\n'.format(char, stack, counter))
        
    while stack:
        ## pop ##
        stack.pop()
        counter += 1
        log.write('pop, {0}, {1}\n'.format(stack, counter))
        
    log.write('---\n')
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
