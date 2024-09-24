N = int(input("How many eggs do you have? ")) 
gross = N // 144
dozen = (N % 144) // 12
leftover = N % 12  
print("Gross:",gross,"dozen:",dozen,"leftover:",leftover)