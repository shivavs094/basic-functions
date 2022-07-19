def naive_search(l,target):
    for i in range(len(l)):
        if l[i]==target:
            return i
    return "No data"

def binary_search(l,target,low=None,high=None):
    if low is None:
        low =0
    if high is None:
        high=len(l)-1
    if high<low:
        return 'Not avilable'

    miodpoint=(low+high)//2

    if l[miodpoint]==target:
        return mio dpoint
    elif target < l[miodpoint]:
        return binary_search(l,target,low ,miodpoint-1)
    else:
        return binary_search(l,target,miodpoint+1,high)

if __name__=='__main__':
    l=[22,25,26,27,65,35,30,20]
    target = 25
    print(binary_search(l,target))
    print(naive_search(l,target))
