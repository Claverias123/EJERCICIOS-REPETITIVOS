import random

numero=random.randint(1,100)
num=0
errores=0

while(numero!=num and errores<10):
    errores +=1
    num=int(input("Dime un número: \n"))
    if(numero<num):
        print("El número es menor")
    else:
        print("El número es mayor")

if(errores==10):
    print(f"Has llegado al límite de intentos. El número era {numero}")
else:
    print(f"Ya lo has adivinado. Lo has acertado despues de {fallos} intentos")