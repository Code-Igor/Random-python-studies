#1

#texto = "hello world"

#print(texto)


#2

#num = input ("informe o número: ")

#print("o número informado foi", num)

#3

#num1 = int(input ("informe um número: "))
#num2 = int(input ("informe um número: "))

#soma = num1 + num2

#print("a soma dos números é", soma)

#4

#num1 = float(input("informe uma nota: "))
#num2 = float(input("informe uma nota: "))
#num3 = float(input("informe uma nota: "))
#num4 = float(input("informe uma nota: "))

#soma = (num1 + num2 + num3 + num4)/4

#print("a média é", soma)

#5

#num1 = float(input("informe um valor em metros: "))
#oma = num1 * 100 

#print("o valor, em centímetros, é de:", soma)

#6

#raio = float(input("informe um valor do raio de um círculo: "))

#soma = 3.14*raio**2

#print("o valor da área é de: ", soma)

#7

#L = float(input("informe o valor de um lado do quadrado: "))

#soma = (L*L)*2

#print("o valor do dobro da área do quadrado é de: ", soma)

#8

#ganho = float(input("informe o seu valor salarial por hora: "))

#horas = float(input("informe a quantidade de horas que você trabalha num mês: "))

#total = ganho*horas

#print("o total do seu salário no referido mês é de: ", total)

#9

#gf = float(input("informe o valor em graus Fahrenheit que deseja converter: "))

#conversão = (gf-32)*5/9

#print("o valor em graus Celsius é de: ", conversão)

#10

#gc = float(input("informe o valor em graus Celsius que deseja converter: "))

#conversão = (gc*9/5) + 32

#print("o valor em graus Fahrenheit é de: ", conversão)

#11

#h = float(input("informe o valor da sua altura: "))

#soma = (72.7*h) - 58

#print("o seu peso ideal é de: ", soma)

#12

#h = float(input("informe o valor da sua altura: "))

#g = (input("qual o seu gênero? (M ou G) "))

#if g == "M":
  #soma = (72.7*h)-58
  #print("o seu peso ideal é de ", soma)
#else:
  #soma = (62.1*h)-44.7
  #print("o seu peso ideal é de ", soma)
  

#13

#peso = float(input("informe o peso de peixes: "))

#ex = 50
#multa = 4

#if peso>ex:
  #conta = (peso-ex)*multa 
  #exc = peso-ex
  #print("excedeu: ",exc, "kg","logo deu ",conta,"R$ de multa.")
#else:
  #print("sem multa.")


#14

#import math

#m = float(input("informe o valor, em metros quadrados, da área a ser pintada: "))

#c = m/3

#tl = float(c/18)

#tp = (math.ceil(tl))*80


#print("A quantidade de latas de tintas a serem compradas será de", math.ceil(tl))
#print("O total será de", tp, "R$")

#15

import math

m = float(input("informe o valor, em metros quadrados, da área a ser pintada: "))

flg = m*1.1

m = flg

c = m/6

#######
#lt = float(c/18)

#ltp = (math.ceil(lt))*80

#g = float(c/3.6)
#gp = (math.ceil(g))*25

#print("A quantidade de latas de tintas a serem compradas será de", math.ceil(lt))
#print("O total será de", ltp, "R$")

#print("A quantidade de galões de tintas a serem compradas será de", math.ceil(g))
#print("O total será de", gp, "R$")
########

#c #usar %%%

lt = float(c/18)
ltp = (math.ceil(lt))*80

gelt = float(c%18)

if gelt>0:
  gl = gelt/3.6
  gp = (math.ceil(gl))*25
  
  total = ltp+gp
  print("A quantidade de latas de tintas a serem compradas será de", math.ceil(lt))
  print("A quantidade de galões de tintas a serem compradas será de", math.ceil(gl))
  print("O total será de", total, "R$")
else:
  print("A quantidade de latas de tintas a serem compradas será de", math.ceil(lt))
  print("O total será de", ltp, "R$")
  
  
  