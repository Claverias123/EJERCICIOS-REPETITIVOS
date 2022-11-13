num=0
num1=0
cont=0
M=0
igual=0
m=0

num=int(input("Cantidad de números que vas a introducir: \n"))

while(num!=cont):
    num1=int(input("Dime un número: \n"))
    cont +=1
    if (num1<0):
        m +=1

    elif(num1>0):
        M +=1

    elif (num1==0):
        igual +=1

print(f"Has introducido {m} número/s menor/es que 0, {M} mayor/es que 0 y {igual} igual/es a 0")