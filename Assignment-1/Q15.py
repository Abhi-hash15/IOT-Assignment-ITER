a=int(input("enter a: "))
b=int(input("enter b: "))
c=a-b
flag=(c>>31)&1
largest=(a*(1-flag)+b*flag)
print(largest)
