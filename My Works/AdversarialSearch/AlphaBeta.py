def minimax(alpha:float, beta:float, data:list, maximizer:bool ) -> float:
    if len(data)==1: return data[0]

    mid:int = len(data)//2
    for child in [ data[:mid], data[mid:] ]:
        if alpha>beta: return alpha if maximizer else beta
        res:float = minimax(alpha,beta,child, not maximizer)
        if maximizer and alpha<res: alpha=res
        elif not maximizer and beta>res: beta=res
    return alpha if maximizer else beta

print(minimax(
    alpha=-1e10,
    beta=1e10,
    data=[1,2,3,4,5,6,7,8],
    maximizer=True
))