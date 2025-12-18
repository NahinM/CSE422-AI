import sys
sys.stdin = open("input.txt","r")
import heapq

def solve():
    n,m = list(map(int,input().split()))
    A,B = list(map(int,input().split()))
    C,D = list(map(int,input().split()))
    maze = [input() for _ in range(n)]
    # print(maze)
    q = []
    vst = [[False]*m for _ in range(n)]
    heapq.heappush(q,(0,0,A,B,""))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    P = ["U","R","D","L"]
    step = 0
    while bool(q):
        step+=1
        hcost,cost,r,c,path = heapq.heappop(q)
        vst[r][c] = True
        # print(f"step{step}")
        if r == C and c==D:
            print(cost,path)
            return
        for i in range(4):
            nr,nc = r+dx[i], c+dy[i]
            if not (0<=nr<n and 0<=nc<m): continue
            if vst[nr][nc] or maze[nr][nc]=='#': continue
            hu = abs(nr-C)+abs(nc-D)
            heapq.heappush(q,((cost+1+hu),(cost+1),nr,nc,path+P[i]))
    print("-1")

t:int = 1
t = int(input())
while t>0:
    t-=1
    solve()