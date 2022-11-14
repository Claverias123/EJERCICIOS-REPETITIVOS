h=0
d=0
trs=0
s=0
ttl=0

h=(int)(input("¿Cuántas horas trabajas al día?\n"))
d=(int)(input("¿Cuántos días trabajas?\n"))
trs=(int)(input("¿Cuántos trabajadores hay en la empresa?\n"))
s=(int)(input("¿Cuanto se cobra por hora?\n"))

for i in range(0,d):
    ttl=ttl+(h*s)

print("Esta semana tu sueldoes:",ttl)
print("Por" ,trs, " la empresa ha pagado:" ,trs*ttl,)