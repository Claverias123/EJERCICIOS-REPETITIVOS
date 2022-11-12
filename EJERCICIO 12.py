total=0
cont=0

for i in range(1,13):
    num=int(input("Dime el dinero que has ahorrado\n"))
    total=total+num
    cont=cont+1
    print("El dinero ahorrado en este mes", cont,"es de", total)
print("El dinero que has ahorrado en este año es", total)