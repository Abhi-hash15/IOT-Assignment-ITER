weight=float(input("enter weight(in kg): "))
height=float(input("enter height(in mt): "))
pd=0.45359237*weight
inch=0.0254*height
bmi=pd/inch*inch
print(bmi)
