'''
Realizar una algoritmo que muestre la tabla de multiplicar de un número
introducido por teclado.
'''
num=0
num=int(input("Dime un numero\n"))
lim=int(input("Dime hasta donde quieres multiplicar\n"))
print("**********************")


for num1 in range (0,lim):
    print(num,"*", num1,"es", num*num1)