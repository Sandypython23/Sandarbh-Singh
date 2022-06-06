l1 = eval(input("enter your list"))
for i in range(0,len(l1)):
    for j in range(0,len(l1)):
        if(l1[i]==l1[j] and i != j):
            print("the number being repeated is",l1[j])
