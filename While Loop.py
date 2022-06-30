num=0
i=0

while  i<4:
    num= int(input("number_"))
    if num==0:
        print("square:0")
        i+=1
        continue
    if num== 1:
            print("program exited")
            break
    sq=str(num*num)
    print("square:",sq )
    i+=1
else:
    print("Done")