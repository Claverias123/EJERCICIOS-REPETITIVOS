vNum=[]
num_pri=0
numeroprimo = (int)(input("Dime un número:\n"))
i=2
cont=numeroprimo

def num_primo(num):
    num_primo=0
    for i in range(2, num):
        if num%i==0:
            num_primo +=1
    if num_primo >= 1:
        return False
    else:
        return True

while cont!=0:
    if num_primo(i)==True:
        vNum.append(i)
        cont-=1
    i+=1
print(vNum)


