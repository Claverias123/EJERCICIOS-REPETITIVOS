'''
Escribir un programa que imprima todos los números pares entre dos números
que se le pidan al usuario.
'''
num=0
num1=int(input("Dime un numero\n"))
num2=int(input("Dime otro numero\n"))

print("Los numeros pares son:")

for num in range(num1,num2+1):
    if num%2==0:
        print(num)
   
        