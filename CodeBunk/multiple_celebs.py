import random
N = 100
#prepare testcase
R = range(N)
rand_celeb = list(set(random.randint(0,N-1) for i in xrange(5)))

m = {}
for i in xrange(N):
    if i not in rand_celeb:
        m[i] = [random.randint(0,N-1) for j in xrange(10)] +rand_celeb
    else:
        m[i] = []

def knows(i,j): #i knows j?
    return j in m[i]

def find_celebs(n):
    celeb = 0
    for i in xrange(1,n):
        if not knows(i,celeb):
            celeb = i
    celebs = []
    for i in xrange(n):
        if i != celeb and knows(celeb,i):
            return None
        if not knows(i,celeb):
            celebs.append(i)
    return celebs

print R
print "Actual Celeb : ",rand_celeb
print "Found Celeb : ",find_celebs(len(R))
