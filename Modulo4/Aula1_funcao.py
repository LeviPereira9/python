def fibonnaci(end):
    if(end == 1 or end == 0):
        return end
    
    return fibonnaci(end - 1) + fibonnaci(end - 2)


print(fibonnaci(8))