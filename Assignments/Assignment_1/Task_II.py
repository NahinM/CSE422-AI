import sys
sys.stdin = open("input2.txt","r")
import heapq

def solve():
    n,m = list(map(int,input().split()))
    a,b = list(map(int,input().split()))
    heuristic = [0]*(n+1)
    for _ in range(n):
        x,y = list(map(int,input().split()))
        heuristic[x]=y
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v = list(map(int,input().split()))
        graph[u].append(v)
        graph[v].append(u)
    
    q = []
    vst = [False]*(n+1)
    vst[b] = True
    inadmissable = []
    heapq.heappush(q,(0,b))
    while bool(q):
        cost,at = heapq.heappop(q)
        if heuristic[at]>cost:
            inadmissable.append(str(at))
        for e in graph[at]:
            if vst[e]: continue
            vst[e] = True
            heapq.heappush(q,(cost+1,e))
    if bool(inadmissable):
        print("0")
        print(f"Here nodes {','.join(inadmissable)} are in admissable.")
    else:
        print("1")

t:int = 1
t = int(input())
cas = 1
while t>0:
    t-=1
    ignore = input()
    print(f"--- Test case{cas} ---")
    cas+=1
    solve()
    print()