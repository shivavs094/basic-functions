def divis (a,b):
    print (a/b)

def smart_divis(func):

    def inner (a,b):
        if a>b:
            a,b=b,a
        return func(a,b)

    return inner

divis=smart_divis(divis)
divis(2,4)