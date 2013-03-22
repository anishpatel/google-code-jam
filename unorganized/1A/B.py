from fractions import Fraction

FILE_NAME = 'B-sample'
#FILE_NAME = 'B-small-practice'
#FILE_NAME = 'B-small-attempt0'
#FILE_NAME = 'B-large'

def do_case(words, num_words, ls, lens):
    points = [0] * num_words
    for char in ls:
        for i in xrange(num_words):
            if char in words[i]:
                words[i].remove(char)
            elif words[i]:
                points[i] += 1
        for l in lens:
            if len(tuple(True for i in lens[l] if words[i])) <= 1:
                for i in lens[l]:
                    words[i] = set()
    return points.index(max(points))

with open('{0}.in'.format(FILE_NAME), 'r') as inpt:
    with open('{0}.out'.format(FILE_NAME), 'w') as out:
        T = int(inpt.readline()[:-1])
        for t in xrange(1, T+1):
            num_words, num_lists = (int(value) for value in inpt.readline()[:-1].split())
            words = [inpt.readline()[:-1] for i in xrange(num_words)]
            #short_words = [set(word) for word in words]
            lists = [inpt.readline()[:-1] for i in xrange(num_lists)]
            lens = dict()
            for l in set(len(word) for word in words):
                lens[l] = [i for i in xrange(num_words) if len(words[i]) == l]
            out.write('Case #{0}:'.format(t))
            for ls in lists:
                index = do_case([set(word) for word in words], num_words, ls, lens)
                out.write(' {0}'.format(words[index]))
            out.write('\n')

print 'done.'
