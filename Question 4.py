def doublestr(str1):
    str2 = ''
    for i in range(0,len(str1)):
        str2 = str2 + str1[i]*2
        if(i==len(str1)-1):
            print(str2)

str1 = input("enter your string")
doublestr(str1)
