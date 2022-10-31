numero=int(input("Dime un número\n"))
rst=1

for num in range(1,numero+1):
    rst= rst*num

print(f"La factorial de {numero} es {rst}")