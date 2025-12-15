def minimax( data:list, maximizer:bool ) -> int:
    if len(data)==1: return data[0]
    mid:int = len(data)//2
    if maximizer: return max( minimax(data[:mid],not maximizer), minimax(data[mid:],not maximizer) )
    else: return min( minimax(data[:mid],not maximizer), minimax(data[mid:],not maximizer) )

print(minimax(
    data=[1,2,3,4,5,6,7,8],
    maximizer=True
    ))