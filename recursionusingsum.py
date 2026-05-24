def sum(x,y):
    if y==1:
        return x
    elif x==1:
        return x
    elif x==0 or y==0:
        return 0
    else:
        return x+sum(x,y-1)
print(sum(10,8))    
    
    
    
    