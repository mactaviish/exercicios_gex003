lista=[[],[],[]]
aposta=[[],[],[]]
acerto=0

print("Digite o Gabarito:")
for cont in range(13):
	cond=0
	num=int(input(""))
	if num != 1 and num !=2 and num !=3:
		while cond == 0:
			num=int(input())
			if num == 1 or num == 2 or num == 3:
				cond+=1
	if num == 1:
		lista[0].append(cont)
	if num ==2:
		lista[1].append(cont)
	if num == 3:
		lista[2].append(cont)

print("Digite a Aposta: ")
cont=0
for cont in range(13):
	cond=0
	num=int(input(""))
	if num != 1 and num !=2 and num !=3:
		while cond == 0:
			num=int(input())
			if num == 1 or num == 2 or num == 3:
				cond+=1
	if num == 1:
		aposta[0].append(cont)
	if num ==2:
		aposta[1].append(cont)
	if num == 3:
		aposta[2].append(cont)
cont=0
pos=0
for cont in lista:
	linha=0
	while linha<13:
		if cont[linha] == aposta[pos][linha]:
			acerto+=len(cont)
		linha+=1
	pos+=1
if acerto == 13:
	print("GANHADOR, PARABÉNS")
if acerto != 13:
	print("Número de Acertos: ", acerto)
==================================================================================================================
lista=[]
lista2=[]
lin=4
print("Digite 5 números inteiros: ")
for i in range(5):
	num=int(input())
	lista.append(num)
	lista2.insert(0,num)
print(lista2)
==================================================================================================================
lista=[]
qtd=0

print("Digite 10 números interos: ")
for i in range(10):
	num=int(input())
	lista.append(num)
print("Digite o número alvo: ")
alvo=int(input())
for j in lista:
	if j==alvo:
		qtd+=1
print("Vezes que 'Alvo' aparece no vetor: ",qtd)
==================================================================================================================
lista1=[]
lista2=[]
lista3=[]
lista4=[]
print("Primeira Lista:")
for i in range(9):
	num=int(input())
	lista1.append(num)
print("Segunda Lista:")
for j in range(9):
	num=int(input())
	lista2.append(num)
print("Terceira Lista:")
for k in range(9):
	num=int(input())
	lista3.append(num)
for l in lista1[0:3]:
	lista4.append(l)
for m in lista2[3:6]:
	lista4.append(m)
for n in lista3[6:9]:
	lista4.append(n)
print(lista4)
==================================================================================================================
lista=[]
num1=0
num=int(input())
for i in range(15):
	num1+=num
	lista.append(num1)
print(lista)
==================================================================================================================
