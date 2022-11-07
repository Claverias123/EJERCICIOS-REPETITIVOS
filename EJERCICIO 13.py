total=0
cont=1
sueldo=0
sueldo=int(input("Dime cuanto cobras por hora\n"))
for i in range(1,7):
    num=0
    num=int(input(f"Dime cuantas horas has trabajado el dia {cont}:"))
    cont=cont+1
    total=total+num
print("La cantidad de horas que has trabajado a la semana es de:", total)
print("El sueldo que has ganado a la semana es de:", total*sueldo,"euros")


