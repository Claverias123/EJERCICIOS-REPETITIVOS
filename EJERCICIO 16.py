ttl=0
ttlP=0
trabajadores=0
sueldo=0
contTrabajadores=1
num=0


trabajadores=int(input("Dime cuantos trabajadores hay:"))
sueldo=int(input("Dime cuanto cobra por hora:"))

for i in range(trabajadores):    
    num=int(input(f"Dime cuantas horas ha trabajado en esta semana el trabajador {contador_trabajador}:"))
    contTrabajadores=contTrabajadores+1
    ttl=sueldo*num
    ttlP+=total
    print(f"El sueldo semanal del trabajador {contador_trabajador} es de: {total}")

print("El sueldo semanal total es de:",ttlP,"€")