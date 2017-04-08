import json 
import random
import sys, time


def mostra_ipmon(ipmon,a):
	print("Nome = {0}".format(ipmon[a]["nome"]))
	print("Atk = {} e vale {}".format(ipmon[a]["Atk"][0],ipmon[a]["Atk"][1]))
	print("def = {0}".format(ipmon[a]["def"]))
	print("hp = {0}\n".format(ipmon[a]["hp"])) 

def batalha(inspermons, outros, SuasInfo, Insperdex):
	adversario = str(random.choice(outros))
	VidaAdversarioInicial = inspermons[adversario]["hp"]
	print("Um inimigo quer batalhar...\n")
	InfoAdversario = mostra_ipmon(inspermons,adversario)
	Vontade = input("Digite N se deseja fugir da batalha, ou pressione Enter para continuar")
	if Vontade == "N" or Vontade == "n":
		print("\nVocê fugiu da batalha")
	else:
		Inimigo = inspermons[adversario]
		x = 0
		while Inimigo["hp"] > 0  and SuasInfo["hp"] > 0:
			if x%2 == 0:
				print("----------------------------\n  Placar:\n    Hp do seu pokémon: {}\n    Hp do inimigo: {}\n----------------------------\n".format(SuasInfo["hp"], Inimigo["hp"]))
				TipodeAtk = input("Escolha o ataque que deseja usar: \n 1.{}".format(SuasInfo["Atk"][0]))
				Inimigo["hp"] = Inimigo["hp"] - (SuasInfo["Atk"][1]-Inimigo["def"])
				x += 1
				if TipodeAtk == "1":
					print("\n{} usou {}. Foi super efetivo!\n".format(SuasInfo["nome"],SuasInfo["Atk"][0]))
					if Inimigo["hp"] <= 0:
						print("\nVocê ganhou a batalha!\n")
						if inspermons[adversario] not in Insperdex:
							Insperdex.append(inspermons[adversario])
							print("Esse pokémon foi adicionado na sua pokédex.")
							inspermons[adversario]["hp"] = VidaAdversarioInicial
			else:
				SuasInfo["hp"] = SuasInfo["hp"] - (Inimigo["Atk"][1]-SuasInfo["def"])
				x += 1
				print("{} usou {}. Foi super efetivo!\n".format(Inimigo["nome"],Inimigo["Atk"][0]))
				if SuasInfo["hp"] <= 0:
					print("\nSeu pokémon desmaiou, reviva ele no PokéCenter")
					SuasInfo["hp"] = 0

def printfala(texto):
    for x in texto:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.01)
    print
with open('Insper.json') as arquivo: 
	inspermons = json.load(arquivo) 

Inicio = input("--------------------------------------\n  * Qual você escolhe para começar? *\n-------------------------------------- \n 1.Bullbasaur \n 2.Charmander \n 3.Squirtle \n Digite o número: ")
SuasInfo = inspermons[Inicio]
VidaInicial = SuasInfo["hp"]
print("\nAs suas informações são:")
mostra_ipmon(inspermons, Inicio)
Insperdex = [SuasInfo]
outros = list(range(1,11))


while True:
	Menu = input("1.Agir \n2.Ver Pokédex \n3.Administrar pokémons \n4.Status do Pokémon Principal \n   Digite o número: ")
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
		Fazer = input("\nO que você quer fazer? \n 1.Passear \n 2.Dormir? \n 3.Ir para um PokéCenter\n 4.Voltar \n Digite o número: ")
		print("\n")
		if Fazer == "2":
			print("Até a próxima!")
			break
		if Fazer=="4":
			continue
		elif Fazer == "3":
			printfala("Nurse Joy: Oi! Deseja reviver seu pokémon?\n")
			Desejo = input("S/N ")
			if Desejo == "S" or Desejo == "s":
				SuasInfo["hp"] = VidaInicial
				printfala("\nA vida do seu pokémon foi restaurada!")
			if Desejo == "N" or Desejo == "n":
				printfala("\nVolte sempre!")
		elif Fazer == "1" and SuasInfo["hp"] > 0:
			batalha(inspermons, outros, SuasInfo, Insperdex)
		else:
			print("Você não pode batalhar com seu Pokémon desmaiado!")
	print("\n**********************************************************\n")