vNum=[]
num_primo=0
cont = (int)(input("Dime un número:\n"))
i=2

def num_primo(num):
    for i in range(2, num):
        if num%i==0:
            cont +=1
    if cont >= 1:
        return False
    else:
        return True

while cont!=0:
    if num_primo(i)==True:
        cont-=1
        print(i)
    i+=1


