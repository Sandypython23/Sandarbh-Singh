Str = eval(input("enter your string"))
sum1 = 0
for i in range(0,len(Str)):
    if(Str[i].isdigit() == True):
        sum1 = sum1 + int(Str[i])
        if(i==len(Str)-1):
            print("the sum of all the integer values in string : ", sum1)
        
        
        
    
        
        
