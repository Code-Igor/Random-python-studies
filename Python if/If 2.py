#2

#a

#n1 = int(input("Insira um número inteiro: "))
#n2 = int(input("Insira um outro número inteiro: "))

#if n1>n2: 
  #n3 = n1-n2
  #print(n3)
#else:
  #n4 = n2-n1
  #print(n4)

#b

#n1 = int(input("Insira um número: "))

#if n1>=0:
  #print(n1)
#else:
  #n2 = n1*(-1)
  #print(n2)

#c

#n1 = float(input("Insira o valor da nota do aluno: "))
#n2 = float(input("Insira o valor da nota do aluno: "))
#n3 = float(input("Insira o valor da nota do aluno: "))
#n4 = float(input("Insira o valor da nota do aluno: "))

#m = (n1+n2+n3+n4)/4

#if m >= 5:
  #print("Parabéns, você foi aprovado! O valor da média foi de: ",m)
#else:
  #print("Infelizmente você foi reprovado! O valor da média foi de: ",m)

#d

#n1 = int(input("Insira um número: "))
#n2 = int(input("Insira um número: "))
#n3 = int(input("Insira um número: "))
#n4 = int(input("Insira um número: "))

#d1 = n1/2  
#d12 = n1/3
#d1i = int(n1/2)
#d12i = int(n1/3)

#d2 = n2/2  
#d22 = n2/3
#d2i = int(n2/2)
#d22i = int(n2/3)

#d3 = n3/2  
#d32 = n3/3
#d3i = int(n3/2)
#d32i = int(n3/3)

#d4 = n4/2  
#d42 = n4/3
#d4i = int(n4/2)
#d42i = int(n4/3)


#if d1 == d1i and d12 == d12i:
  #print("é divisível por 2 e por 3")
#else:
  #print("Não é divisível por 2 e 3")

#if d2 == d2i and d22 == d22i:
#  print("é divisível por 2 e por 3")
#else:
#  print("Não é divisível por 2 e 3")

#if d3 == d3i and d32 == d32i:
 # print("é divisível por 2 e por 3")
#else:
 # print("Não é divisível por 2 e 3")

#if d4 == d4i and d42 == d42i:
  #print("É divisível por 2 e por 3")
#else:
 # print("Não é divisível por 2 e 3")

  
#e forma de fazer o d mais simples tbm

#n1 = int(input("Insira um número: "))
#n2 = int(input("Insira um número: "))
#n3 = int(input("Insira um número: "))
#n4 = int(input("Insira um número: "))

#d1 = n1/2
#d2 = n2/2
#d3 = n3/2
#d4 = n4/2

#d1s = n1/3
#d2s = n2/3
#d3s = n3/3
#d4s = n4/3

#if d1 == int(d1) or d1s == int(d1s):
 #print(n1, "é divisível por 2 ou por 3")
#else:
  #print(n1, "não é divisível por 2 e por 3")

#if d2 == int(d2) or d2s == int(d2s):
  #print(n2, "é divisível por 2 ou por 3")
#else:
  #print(n2, "não é divisível por 2 e por 3")

#if d3 == int(d3) or d3s == int(d3s):
  #print(n3, "é divisível por 2 ou por 3")
#else:
  #print(n3, "não é divisível por 2 e por 3")

#if d4 == int(d4) or d4s == int(d4s):
  #print(n4, "é divisível por 2 ou por 3")
#else:
  #print(n4, "não é divisível por 2 e por 3")


#f

#age = int(input("Insira sua idade: "))

#if age < 5:
 # print("Inadequado")
#if age >= 5 and age <= 7:
#  print("Infantil A")
  
#if age >= 8 and age <= 10 :
#  print("Infantil B")

#if age >= 11 and age <= 13 :
#  print("Juvenil A")

#if age >= 14 and age <= 17 :
#  print("Juvenil B")

#if age >= 18 and age <= 60 :
 # print("Adulto")

#if age >= 60:
 # print("Senior")

#g

##ax² + bx + c = 0

#import math
#square_root = math.sqrt

#a = float(input("Informe o valor de a: ")) 
#b = float(input("Informe o valor de b: "))
#c = float(input("Informe o valor de c: "))

#if a == 0:
 # print("Não é uma equação de segundo grau.")
#else:
#  delta = (b**2)-4*a*c
  
#  x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
#  x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
#  print("x1 = ",x1)
#  print("x2 = ",x2)

#h

#p1n = input("Insira o nome do produto: ") 
#p1 = float(input("Insira a quantidade desse produto: "))

#p2n = input("Insira o nome do produto: ") 
#p2 = float(input("Insira a quantidade desse produto: "))

#p3n = input("Insira o nome do produto: ") 
#p3 = float(input("Insira a quantidade desse produto: "))

#p4n = input("Insira o nome do produto: ") 
#p4 = float(input("Insira a quantidade desse produto: "))

#if p1 < 30:
 # print(p1n, "está abaixo do estoque mínimo.")
  
#if p2 < 30:
#  print(p2n, "está abaixo do estoque mínimo.")
#if p3 < 30:
 # print(p3n, "está abaixo do estoque mínimo.")
  
#if p4 < 30:
#  print(p4n, "está abaixo do estoque mínimo.")

#a
#resolver as operações

#a = (18/3/2 -1)*5-4-(2 + 3 +5)/2
#print("A:",a)

#b = 266/62-127/7%5
#print("B:",b)

#c = 7%4-8/(3 * 1)
#print("C:",c)


#d = (2 >=5) and (1!=0) and not(6 <= 2*3 ) or (10 != 10)
#print("D:",d)

#e = (5 != 2) or not(7>4) and (4<=3.14)
#print("E:",e)


#h

#num = float(input("Informe um valor numérico: ")) 

#par = num/2 

#if par == int(par):
 #print(num, "é par")
#else:
 #print(num, "não é par")

#a

#n1 = float(input("Informe um número: "))
#n2 = float(input("Informe outro número: "))

#if n1 > n2:
  #print(n1)
#elif n2 > n1:
  #print(n2)
#else:
  #print("Possuem o mesmo valor.")


#j

#x1 = float(input("Insira um valor para x1: "))
#x2 = float(input("Insira um valor para x2: "))

#d1 = x1
#x1 = x2
#x2 = d1 

#print("O novo valor de x1 é: ", x1) 

#print("O novo valor de x2 é: ", x2)


#k

#sb = float(input("Insira seu salário bruto: "))

#sm = 1412

#p = sb*0.1

#if sb <= sm*3:
 # p = sb*0.08
 # inss = sb-p
# print("Com os descontos do INSS: ", inss)

#elif p > sm:
# inss = sb-sm
# print("Com os descontos do INSS: ", inss)
  
#else:
#  inss = sb-p
#  print("Com os descontos do INSS: ", inss)


#3

#sb = float(input("Insira seu salário bruto: "))

#sm = 1412

#p = sb*0.1

#if sb <= sm*3:
  #p = sb*0.08
  #inss = sb-p
  #print("Com os descontos do INSS: ", inss)

#elif p > sm:
 #inss = sb-sm
 #print("Com os descontos do INSS: ", inss)

#else:
  #inss = sb-p
  #print("Com os descontos do INSS: ", inss)



#if inss <=900:
  #print("Com os descontos do IRRF: ",inss)
#elif inss > 1800:
  #q = inss*0.275
  #irrf = inss-q
  #print("Com os descontos do IRRF: ",irrf)
#else:
  #q = inss*0.15
  #irrf = inss-q
  #print("Com os descontos do IRRF: ",irrf)


#n

#p1 = float(input("Insira o valor da nota da prova: "))
#p2 = float(input("Insira o valor da nota prova: "))
#p3 = float(input("Insira o valor da nota prova: "))
#p4 = float(input("Insira o valor da nota prova: "))

#mp = (p1+p2+p3+p4)/4

#t1 = float(input("Insira o valor da nota do trabalho: "))
#t2 = float(input("Insira o valor da nota do trabalho: "))
#t3 = float(input("Insira o valor da nota do trabalho: "))
#t4 = float(input("Insira o valor da nota do trabalho: "))

#mt = (t1+t2+t3+t4)/4

#mf = 0.8*mp + 0.2*mt

#if mf >= 6:
  #print("Aprovado!")
#else:
  #print("Não aprovado!")

#5-3

q = float(input("Insira a nota da qualidade: "))
p = float(input("Insira a nota do preço: "))
pz = float(input("Insira a nota do prazo: "))

ng = (q+p+pz)/3

if q < 7:
  ng = 0
  print("A nota geral é de: ",ng)

elif q >= 7 and p < 7:
  ng = (q+p*2+pz)/4
  print("A nota geral é de: ",ng)
else:
  print("A nota geral é de: ",ng)
