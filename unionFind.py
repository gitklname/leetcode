class UnionFind:
    def __init__(self, n):
        self.father = list(range(n))
        self.count = n
    
    def find(self, x):
        if self.father[x] != x:
            self.father[x] = self.find(self.father[x])
        
        return self.father[x]

    def union(self, p, q):
        p_father = self.find(p)
        q_father = self.find(q)
        if p_father == q_father:
            return
        
        self.father[p_father] = q_father

        self.count -= 1

    def isConnected(self, p, q):
        p_father = self.find(p)
        q_father = self.find(q)
        return p_father == q_father

if __name__ == '__main__':
    pass