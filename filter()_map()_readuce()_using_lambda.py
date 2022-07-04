from functools import  reduce
#def is_even (n):
   # return n%2==0

#def double_2 (n):
    #return n*2

#def all_sum (a,b):
    #return a+b



nums ={2,4,56,44,2,8,7,6,4,8,9,3,2,22,55,44,49,67,}
evens_filter =list(filter(lambda n:n%2==0,nums))
double_map= list (map(lambda m:m*2,evens_filter))

sum =reduce(lambda a,b:a+b,double_map)

print(evens_filter)
print(double_map)
print(sum)