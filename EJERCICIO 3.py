num=1
s=0
cont= -1

print("Escribe número 0 para salir")

while(num!=0): 
    num=int(input("Dime un número: \n"))  
    s=s+num
    cont=cont+1
             
print(f"La suma es {s}")
print(f"La media es {s/cont}")