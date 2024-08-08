n=int(input("enter the number of lines:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,2*i):
        if(i==1 or i==n or k==1 or k==i or k==2*i-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()

n=int(input("enter the number of lines:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end=" ")
    print()