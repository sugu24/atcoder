N = int(input())
S = N*N
T = N*N+1
inf=10**9

from collections import deque
class Dinic:
    def __init__(self,N):
        self.N=N
        self.edge = [[] for _ in range(self.N)]
        
    
    def add_edge(self,fro,to,c):
        self.edge[fro].append([to,inf,len(self.edge[to])])
        self.edge[to].append([fro,0,len(self.edge[fro])-1])
    

    def bfs(self,s):
        self.level = [-1]*(N*N+2)
        self.level[s]=0
        q = deque([s])
        while q:
            fro = q.popleft()
            for to,c,rev in self.edge[fro]:
                if self.level[to]==-1 and c>0:
                    self.level[to]=self.level[fro]+1
                    q.append(to)
                    

    def dfs(self,s,t,f):
        if s==t:return f
        for i in range(self.used[s],len(self.edge[s])):
            self.used[s] = i+1
            to,c,rev=self.edge[s][i]
            if c>0 and self.level[to]>self.level[s]:
                d = self.dfs(to,t,min(f,c))
                if d>0:
                    self.edge[s][i][1]-=d
                    self.edge[to][rev][1]+=d
                    return d
        return 0
    
    
    def max_flow(self,s,t):
        flow = 0
        while True:
            self.bfs(s)
            self.used = [0]*(self.N)
            if self.level[t]<0: return flow
            d = 1
            while d>0:
                d = self.dfs(s,t,inf)
                flow += d


flow = Dinic(N*N+2)
field = [[] for i in range(N)]
for i in range(N):
    temp = input()
    for j in range(N):
        if (i+j)%2==1:
            if temp[j] == 'B':
                field[i].append('W')
            elif temp[j] == 'W':
                field[i].append('B')
            else:
                field[i].append(temp[j])
        else:
            field[i].append(temp[j])

for i in range(N):
    for j in range(N):
        n = i*N+j
        if field[i][j]=='B':
            flow.add_edge(S,n,inf)
        elif field[i][j]=='W':
            flow.add_edge(n,T,inf)
            
        for ni,nj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            nij = ni*N+nj
            if 0<=ni<N and 0<=nj<N and n<nij:
                flow.edge[n].append([nij,1,len(flow.edge[nij])])
                flow.edge[nij].append([n,1,len(flow.edge[n])-1])

print(2*N*(N-1)-flow.max_flow(S,T))