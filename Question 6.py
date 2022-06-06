l1 = int(input("Enter the first point"))
close = int(input("enter the close point"))
for j in range(l1,close+1):
    if(j==1):
        continue
    ct = 1
    for t in range(2,j):
        if(j%t==0):
            ct = 0
            break
    if(ct == 1):
        print(j)
    
        
