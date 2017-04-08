import json 
def mostra_ipmon(ipmon,a):
	print("Nome = {0}".format(ipmon[a]["nome"]))
	print("Atk = {} e vale {}".format(ipmon[a]["Atk"][0],ipmon[a]["Atk"][1]))
	print("def = {0}".format(ipmon[a]["def"]))
	print("hp = {0}\n".format(ipmon[a]["hp"])) 
with open('Insper.json') as arquivo: 
	inspermons = json.load(arquivo) 
Inicio = input("Qual você escolhe para começar? \n 1.Bullbasaur \n 2.Charmander \n 3.Squirtle \n Digite o número:")
SuasInfo= inspermons[Inicio]
VidaInicial= SuasInfo["hp"]
print("As suas informações são:")
mostra_ipmon(inspermons, Inicio)
Insperdex= [SuasInfo]
del inspermons[Inicio]
outros=list(range(1,11))
del outros[int(Inicio)-1]
import random


while True:
	Menu= input("1. Agir \n2.Ver Pokédex \n3. Administrar pokémons \n4.Status do Pokémon Principal")
	if Menu =="2":
		print(Insperdex)
	if Menu == "4":
		mostra_ipmon(Insperdex, 0)
	if Menu == "1":
		Fazer= input("O que você quer fazer? \n 1.Passear \n    OU \n 2.Dormir? \n     OU \n 3.Ir para um PokéCenter \n Digite o número:")
		if Fazer == "2":
			print("Até a próxima!")
			break
		if Fazer == "3":
			Desejo= input("Nurse Joy: Oi! Deseja reviver seu pokémon?  S/N ")
			if Desejo=="S" or Desejo=="s":
				SuasInfo["hp"]=VidaInicial
				print("A vida do seu pokémon foi restaurada!")
				continue
			if Desejo=="N" or Desejo=="n":
				print("Volte sempre!")
				continue
		elif SuasInfo["hp"]>0:
			adversario = str(random.choice(outros))
			print("Um inimigo quer batalhar...")
			InfoAdversario= mostra_ipmon(inspermons,adversario)
			Vontade= input("Digite N se deseja fugir da batalha, ou pressione Enter para continuar")
			if Vontade =="N" or Vontade == "n":
				print("Você fugiu da batalha")
				continue
			Inimigo=inspermons[adversario]
			x=0
			while True:
				if x%2==0:
					TipodeAtk = input("Escolha o ataque que deseja usar: \n 1.{}".format(SuasInfo["Atk"][0]))
					Inimigo["hp"]=Inimigo["hp"] - (SuasInfo["Atk"][1]-Inimigo["def"])
					x+=1
					if TipodeAtk=="1":
						print("{} usou {}. Foi super efetivo!".format(SuasInfo["nome"],SuasInfo["Atk"][0]))
					if Inimigo["hp"]<=0:
						print("Você ganhou a batalha!")
						if inspermons[adversario] not in Insperdex:
							Insperdex.append(inspermons[adversario])
							print("Esse pokémon foi adicionado na sua pokédex.")
							break
						break
				
				else:
					SuasInfo["hp"]=SuasInfo["hp"] - (Inimigo["Atk"][1]-SuasInfo["def"])
					x+=1
					print("{} usou {}. Foi super efetivo!".format(Inimigo["nome"],Inimigo["Atk"][0]))
					if SuasInfo["hp"]<=0:
						print("Seu pokémon desmaiou, reviva ele no PokéCenter")
						break
		else:
			print("Você nao pode batalhar com seu Pokémon desmaiado!")