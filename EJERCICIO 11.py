num = (int)(input("Dime un número:\n"))
cont = 0


for i in range(2, num):
    if num%i==0:
        cont +=1
if cont >= 1:
    print("El número", num,"no es primo")
else:
    print("El número", num ,"es primo")