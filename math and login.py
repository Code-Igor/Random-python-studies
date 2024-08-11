#2 funcionaaaaaaaaaa

#salBase = float(input("informe salário"))
#SalReceber = salBase + (salBase*5/100)
#Imp = SalReceber*7/100
#SalReceber = SalReceber-Imp
#print(SalReceber)

#1 n funcionaaaaaaaaa

#salBase = float(input("informe salário"))
#grat = salBase*5/100
#Imp = SalReceber*7/100
#SalReceber = salBase + grat-Imp
#SalReceber = SalReceber-Imp
#print(SalReceber)

#fazer funcionar:

#salBase = float(input("informe salário "))

#grat = salBase*5/100
#SalReceber = salBase + grat
#Imp = SalReceber*7/100
#SalReceber = SalReceber-Imp
#print(SalReceber)

#3

#import math
#pi = math.pi

#R = float(input("Informe o valor do raio da base do tanque: "))

#H = float(input("Informe o valor da altura do tanque: "))

#ar = float(2*pi*R**2 + 2*pi*R*H)

#L = float(ar/3)

#gl = float(L/3.6)

#glp = math.ceil(gl)*40

#print("A quantidade de galões de tinta será de: ", math.ceil(gl))

#print("O valor será de: ",glp)

#5

#import getpass
#senha = getpass.getpass("Informe a sua senha: ")

#senha = len(senha)

#senha = senha * "*"

#print("Senha: ",senha)

#5.1 test

import getpass

login = input("Escolha um nome de usuário: ")

senha = input("Defina a sua senha: ")

print("Cadastro concluído!")

login1 = input("Usuário: ")

while login1 != login:
  print("Usuário inválido. ")
  login1 = input("Usuário: ")

senhaofc = getpass.getpass("Senha: ")

while senhaofc != senha:
  print("Senha inválida. ")
  senhaofc = getpass.getpass("Senha: ")
  
senha1 = len(senha)
senha1 = senha1 * "*"
print("Senha:", senha1)

print("Login concluído.")