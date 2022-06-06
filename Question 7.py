List = eval(input("enter your list"))
max1=0
res = List[0]
for i in List:
    freq = List.count(i)
    if(freq>max1):
        max1 = freq
        res = i
        print("the most frequent number is",str(res))
       
