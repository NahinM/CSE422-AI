def minimax( data:list, maximizer:bool ) -> int:
    if len(data)==1: return data[0]

    mid:int = len(data)//2
    res:list[int] = [ minimax( child, not maximizer ) for child in [ data[:mid], data[mid:] ] ]
    return max(res) if maximizer else min(res)

print(minimax(
    data=[1,2,3,4,5,6,7,8],
    maximizer=True
))