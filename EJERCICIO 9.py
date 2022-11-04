
from ast import Num
from email.mime import base


bs=int(input("Dime la base\n"))
res=bs
exp=int(input("Dime el exponente\n"))
for num in range(exp-1):
    res*=bs
print("El resultado de la potencia es:",res)
