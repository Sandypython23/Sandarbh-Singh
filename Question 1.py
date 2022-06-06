def listfunction(l1):
    print("enter 'asc' if you want to print list with elements in ascending order")
    print("enter 'desc' if you want to print list with elements in decending order")
    b = input("enter your choice : ")
    l3 = l1.copy()
    if(b=='asc'):
        l3.sort()
        print("The ascending order is",l3)
        print("The default list is",l1)
    if(b=='desc'):
        l3.sort(reverse=True)
        print("The descending order is",l3)
        print("The default list is",l1)

l1 = eval(input("enter your list"))
listfunction(l1)
