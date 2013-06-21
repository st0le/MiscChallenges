import random
N = 10
#prepare testcase
R = range(N)
rand_celeb = random.randint(0,N-1)
m = {}
for i in xrange(N):
    if i != rand_celeb:
        m[i] = [random.randint(0,N-1) for j in xrange(10)] + [rand_celeb]
    else:
        m[i] = []


def knows(i,j): #i knows j?
    return j in m[i]

def find_celeb(n):
    celeb = 0
    for i in xrange(1,n):
        if not knows(i,celeb):
            celeb = i
    
    for i in xrange(n):
        if i != celeb and knows(celeb,i):
            return None
    return celeb

print R
print "Actual Celeb : ",rand_celeb
print "Found Celeb : ",find_celeb(len(R))
