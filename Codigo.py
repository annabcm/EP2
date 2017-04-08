import json 
import random

def mostra_ipmon(ipmon,a):
	print("Nome = {0}".format(ipmon[a]["nome"]))
	print("Atk = {} e vale {}".format(ipmon[a]["Atk"][0],ipmon[a]["Atk"][1]))
	print("def = {0}".format(ipmon[a]["def"]))
	print("hp = {0}\n".format(ipmon[a]["hp"])) 

def batalha(inspermons, outros, SuasInfo, Insperdex):
	adversario = str(random.choice(outros))
	VidaAdversarioInicial = inspermons[adversario]["hp"]
	print("Um inimigo quer batalhar...")
	print("\n")
	InfoAdversario = mostra_ipmon(inspermons,adversario)
	Vontade = input("Digite N se deseja fugir da batalha, ou pressione Enter para continuar")
	if Vontade == "N" or Vontade == "n":
		print("\n")
		print("Você fugiu da batalha")
		return "fuga"
	Inimigo = inspermons[adversario]
	x = 0
	while Inimigo["hp"] > 0  and SuasInfo["hp"] > 0:
		if x%2 == 0:
			TipodeAtk = input("Escolha o ataque que deseja usar: \n 1.{}".format(SuasInfo["Atk"][0]))
			print("\n")
			Inimigo["hp"] = Inimigo["hp"] - (SuasInfo["Atk"][1]-Inimigo["def"])
			x += 1
			if TipodeAtk == "1":
				print("{} usou {}. Foi super efetivo!".format(SuasInfo["nome"],SuasInfo["Atk"][0]))
				print("\n")
				if Inimigo["hp"] <= 0:
					print("Você ganhou a batalha!")
					print("\n")
					if inspermons[adversario] not in Insperdex:
						Insperdex.append(inspermons[adversario])
						print("Esse pokémon foi adicionado na sua pokédex.")
						inspermons[adversario]["hp"] = VidaAdversarioInicial
					return
		else:
			SuasInfo["hp"] = SuasInfo["hp"] - (Inimigo["Atk"][1]-SuasInfo["def"])
			x += 1
			print("{} usou {}. Foi super efetivo!".format(Inimigo["nome"],Inimigo["Atk"][0]))
			print("\n")
			if SuasInfo["hp"] <= 0:
				print("Seu pokémon desmaiou, reviva ele no PokéCenter")
				SuasInfo["hp"] = 0
				return

with open('Insper.json') as arquivo: 
	inspermons = json.load(arquivo) 

Inicio = input("--------------------------------------\n  * Qual você escolhe para começar? *\n-------------------------------------- \n 1.Bullbasaur \n 2.Charmander \n 3.Squirtle \n Digite o número: ")
SuasInfo = inspermons[Inicio]
VidaInicial = SuasInfo["hp"]
print("\n")
print("As suas informações são:")
mostra_ipmon(inspermons, Inicio)
Insperdex = [SuasInfo]
outros = list(range(1,11))


while True:
	Menu = input("1.Agir \n2.Ver Pokédex \n3.Administrar pokémons \n4.Status do Pokémon Principal \n Digite o número: ")
	if Menu == "2":
		for a in range(len(Insperdex)):
			print("{}:".format(a+1))
			mostra_ipmon(Insperdex, a)
	if Menu == "3":
		print("Pokémons disponíveis:")
		for i in range(len(Insperdex)):
			print("{}:".format(i+1))
			mostra_ipmon(Insperdex,i)
		SeuPokemon = input("Selecione o Pokémon Principal:")
		SuasInfo = Insperdex[int(SeuPokemon)-1]
	if Menu == "4":
		mostra_ipmon(Insperdex, int(SeuPokemon)-1)
	if Menu == "1":
		print("\n")
		Fazer = input("O que você quer fazer? \n 1.Passear \n 2.Dormir? \n 3.Ir para um PokéCenter \n Digite o número: ")
		print("\n")
		if Fazer == "2":
			print("Até a próxima!")
			break
		elif Fazer == "3":
			Desejo = input("Nurse Joy: Oi! Deseja reviver seu pokémon?  S/N ")
			if Desejo == "S" or Desejo == "s":
				SuasInfo["hp"] = VidaInicial
				print("\n")
				print("A vida do seu pokémon foi restaurada!")
				continue
			if Desejo == "N" or Desejo == "n":
				print("\n")
				print("Volte sempre!")
				continue
		elif Fazer == "1":
			v = batalha(inspermons, outros, SuasInfo, Insperdex)
			if v == "fuga":
				continue
		else:
			print("Você nao pode batalhar com seu Pokémon desmaiado!")
	print("\n")
	print("**********************************************************")