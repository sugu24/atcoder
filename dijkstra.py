import heapq
path = [[] for _ in range(N)]
inf = 10**9

def dijkstra(fro):
    d = [inf]*N
    d[fro] = 0
    q = [(c,to) for to,c in path[fro]]
    heapq.heapify(q)
    while len(q) > 0:
        v,to = heapq.heappop(q)
        if d[to] > v:
            d[to] = v
            for to_to,to_c in path[to]:
                heapq.heappush(q,(d[to]+to_c,to_to))
        elif d[to] == 0:
            d[to] = v
    if d[fro] == 0:
        d[fro] = -1
    return d[fro]