

def magic_square(n):
    assert n % 2 != 0
    m = [[0]*n for i in xrange(n)]
    i = n/2
    j = n - 1
    k = 0
    while k < n*n:    
        m[i][j] = k + 1
        k += 1

        x = i - 1
        if x < 0 : x = n  - 1
        y = (j + 1) % n
        
        if m[x][y] == 0:
            i,j = x,y
        else:
            
            j = j - 1
            if j < 0: j = n - 1
    return m

def verify(m):
    n = len(m)
    s = sum(m[0])
    for row in m:
        if s != sum(row):
            return False
    c = d = 0
    for i in xrange(n):
        d += m[i][i]
        c += m[i][n-1-i]
    if c != s or d != s: return False
    #transpose
    for row in map(list,zip(*m)):
        if s != sum(row):
            return False
    return True
    
    

m = magic_square(7)
if verify(m):
    for row in m:
        print row
else:
    print "Something went horribly wrong!"

