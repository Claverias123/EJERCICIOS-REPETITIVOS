ttl=0
ttlP=0
trabajadores=0
sueldo=0
contTrabajadores=1
num=0


trabajadores=int(input("Dime cuantos trabajadores hay:\n"))
sueldo=int(input("Dime cuanto cobra por hora:\n"))

for i in range(trabajadores):    
    num=int(input(f"Dime cuantas horas ha trabajado en esta semana el trabajador {contTrabajadores}:"))
    contTrabajadores=contTrabajadores+1
    ttl=sueldo*num
    ttlP+=ttl
    print(f"El sueldo semanal del trabajador {contTrabajadores} es de: {ttl}")

print("El sueldo semanal total es de:",ttlP,"€")