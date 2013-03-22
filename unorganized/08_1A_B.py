from itertools import izip

FILE_NAME = '08_1A_B'

inpt = open('{0}.in'.format(FILE_NAME), 'r')
out = open('{0}.out'.format(FILE_NAME), 'w')

def get_num():
    return int(inpt.readline()[:-1])

def get_iter():
    return (int(i) for i in inpt.readline()[:-1].split(' '))

def get_tuple():
    return tuple(int(i) for i in inpt.readline()[:-1].split(' '))

def print_case(case_num, result):
    out.write('Case #{0}: {1}\n'.format(case_num, result))

num_cases = int(inpt.readline()[:-1]) + 1
for case_num in xrange(1, num_cases):
    num_flavors = get_int()
    num_customers = get_int()
    customers = []
    for c in xrange(num_customers):
        customer = []
        it = get_iter()
        num_milkshakes = it.next()
        for ms in xrange(num_milkshakes):
            customer.append( (it.next(), it.next()) )
        customers.append(customer)
    print_case(case_num, )

print 'done.'
inpt.close()
out.close()
