import sys
sys.stdin = open("input1.txt","r")

def utility( gene:list[str] ) -> float:
    global Terget, W
    total:int = 0
    for i in range(len(gene)):
        total+= W[i]*abs(ord(gene[i])-ord(Terget[i]))
    return -total

def minimax( alpha:float, beta:float, pool:list[str], current:list[str], maximizer:bool) -> tuple[float,list]:
    global Terget, W
    if len(pool)==0: return utility(current),current
    ans = []
    for g in pool:
        if alpha>beta: return (alpha,ans) if maximizer else (beta,ans)
        res,state = minimax( alpha, beta, [ a for a in pool if a!=g], current+[g], not maximizer)
        if maximizer and alpha<res:
            alpha=res
            ans = state
        elif not maximizer and beta>res:
            beta=res
            ans = state
    return (alpha,ans) if maximizer else (beta,ans)

Terget:list[str] = []
W:list[int] = []

def solve():
    global Terget, W
    input_pool = input().split(',')
    Terget = [c for c in input()]
    W = [int(c) for c in input().split(' ')][-4:]
    print(minimax(
    alpha=-1e10,
    beta=1e10,
    pool=input_pool,
    current=[],
    maximizer=True
))

t:int = 1
t = int(input())
while t>0:
    t-=1
    solve()