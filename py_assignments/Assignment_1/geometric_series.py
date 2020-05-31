a=float(input("Enter first term of geometric series:"))
r=float(input("Enter common ratio:"))
i=1
while i<=10:
    s=a*(r**i-1)/(r-1)              #formula of geometric series
    print(s)
    print("\n")
    i=i+1
