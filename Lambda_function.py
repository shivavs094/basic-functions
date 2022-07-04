def addition (a,*b):
    c=a
    for i in b:
        c=c+i
    return  c


result= addition (1,2,3,-4,5)
print(result)