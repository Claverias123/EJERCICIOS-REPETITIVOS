import random
num=random.randint(1,100)
num1=0
intentos=1
num1=int(input("Dime un número\n"))

while num1!=num and intentos!=10:
    num1=int(input("Dime otro número\n"))
    if num1>num:
        print("El numero que buscas es menor")
    if num<num:
        print("El numero que buscas es mayor")
    if num1==num:
        print("Has acertado el numero random")
    intentos+=1
if intentos>10:
    print("El número que buscabas era", num)
if intentos<10:
    print("Lo has acertado en", intentos, "intentos")

    