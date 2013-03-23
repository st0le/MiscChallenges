class UnionFind:

    def __init__(self,size):
        self.rank = [-1] * size
        self.size = self.initsize = size

    def find(self,i):
        if self.rank[i] < 0:
            return i
        else:
            self.rank[i] = self.find(self.rank[i])
            return self.rank[i]
        
    def union(self,i,j):
        pi,pj = self.find(i),self.find(j)
        if pi != pj:
            self.size = self.size - 1
            if self.rank[pi] > self.rank[pj]:
                self.rank[pj] += self.rank[pi]
                self.rank[pi] = pj
            else:
                self.rank[pi] += self.rank[pj]
                self.rank[pj] = pi

    def __repr__(self):
        return self.rank

    def __str__(self):
        return str(self.rank)

    def connected(self,i,j):
        return self.find(i) == self.find(j)

    def size(self):
        return self.size

    def set_containing(self,i):
        pi = self.find(i)
        return filter(lambda j : self.rank[j] == pi or j == pi, xrange(self.initsize))

    def disjoint_sets(self):
        ds = []
        for root in filter(lambda j: self.rank[j] < 0, xrange(self.initsize)):
            ds.append(self.set_containing(root))
        return ds        

uf = UnionFind(2001)

for line in open("derpsons.txt"):
    l = map(int,line.split(","))
    for i in l:
        uf.union(i,l[0])

print uf.disjoint_sets()
