n=int(input("Enter the n value: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,"",end="")
    print("\n")

for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print(j,"",end="")
    print("\n")
