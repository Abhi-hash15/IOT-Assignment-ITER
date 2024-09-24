# using arithmetic operators
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
a = a + b
b = a - b
a = a - b
print("after swapping ",a,b)

# using XOR 
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
a = a ^ b
b = a ^ b
a = a ^ b
print("after swapping ",a,b)