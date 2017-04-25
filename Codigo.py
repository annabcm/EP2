import json 
import random
import pickle
import os.path


#Função para mostrar os dados do seu Pokemón
def mostra_ipmon(ipmon,a):
	print("Nome = {0}".format(ipmon[a]["nome"]))
	print("Atk = {}, {} damage".format(ipmon[a]["Atk"][0],ipmon[a]["Atk"][1]))
	print("Spc_Atk = {}, {} damage".format(ipmon[a]["Spc_Atk"][0],ipmon[a]["Spc_Atk"][1]))
	print("Defense = {0}".format(ipmon[a]["def"]))
	print("Health Points = {0}\n".format(ipmon[a]["hp"])) 


# Função sorteia um número aleatório
def sorte():
	luck = random.randint(0,10)
	return luck


#Função da batalha
def batalha(inspermons, outros, SuasInfo, Insperdex,xp):
	adversario = str(random.choice(outros))
	VidaAdversarioInicial = inspermons[adversario]["hp"]
	print("Um inimigo quer batalhar...\n")
	InfoAdversario = mostra_ipmon(inspermons,adversario)
	Vontade = input("Digite N se deseja fugir da batalha, ou pressione Enter para continuar")
	if Vontade == "N" or Vontade == "n":
		print("\nVocê fugiu da batalha")
		return "fuga"
	else:
		Inimigo = inspermons[adversario]
		x = 0
		while Inimigo["hp"] > 0  and SuasInfo["hp"] > 0:
			
			if x%2 == 0:
				print("----------------------------\n  Placar:\n    Hp do seu pokémon: {}\n    Hp do inimigo: {}\n----------------------------\n".format(SuasInfo["hp"], Inimigo["hp"]))
				TipodeAtk = input("Escolha o ataque que deseja usar: \n 1.{} \n 2.{}: \n".format(SuasInfo["Atk"][0],SuasInfo["Spc_Atk"][0]))
				luck = sorte()
				if TipodeAtk == "1": 
					
					if luck < 2:
						Inimigo["hp"] = Inimigo["hp"]
						print ("Seu ataque não atingiu o adversário!")
						x += 1
					if luck > 1 and luck < 8:
						Inimigo["hp"] = Inimigo["hp"] - (SuasInfo["Atk"][1]*(xp/100)-Inimigo["def"])
						print("\n{} usou {}. Foi efetivo!\n".format(SuasInfo["nome"],SuasInfo["Atk"][0]))
						x += 1
					if luck > 7:
						Inimigo["hp"] = Inimigo["hp"] - (SuasInfo["Atk"][1]*(xp/100)+5-Inimigo["def"])
						print("\n{} usou {}. Foi super efetivo!\n".format(SuasInfo["nome"],SuasInfo["Atk"][0]))
						x += 1
					if Inimigo["hp"] <= 0:
						print("\nVocê ganhou a batalha!\n")
						xp = xp + 4
						print ("Você adquiriu o xp! Se você quiser saber mais sobre xp vá para o PokéCenter!")
						if inspermons[adversario] not in Insperdex:
							Insperdex.append(inspermons[adversario])
							print("Esse pokémon foi adicionado na sua pokédex.")
							inspermons[adversario]["hp"] = VidaAdversarioInicial
							break
				
				if TipodeAtk == "2":
					if luck < 2:
						Inimigo["hp"] = Inimigo["hp"]
						print ("Seu ataque não atingiu o adversário!")
						x += 1
					if luck > 1 and luck < 8:
						Inimigo["hp"] = Inimigo["hp"] - (SuasInfo["Atk"][1]*(xp/100)-Inimigo["def"])
						print("\n{} usou {}. Foi efetivo!\n".format(SuasInfo["nome"],SuasInfo["Spc_Atk"][0]))
						x += 1
					if luck > 7:
						Inimigo["hp"] = Inimigo["hp"] - ((SuasInfo["Atk"][1]*(xp/100)+5)-Inimigo["def"])
						print("\n{} usou {}. Foi super efetivo!\n".format(SuasInfo["nome"],SuasInfo["Spc_Atk"][0]))
						x += 1
				
					if Inimigo["hp"] <= 0:
						print("\nVocê ganhou a batalha!\n")
						xp = xp + 4
						print ("Você adquiriou xp! Se você quiser saber mais sobre xp vá para o PokéCenter!")
						if inspermons[adversario] not in Insperdex:
							Insperdex.append(inspermons[adversario])
							print("Esse pokémon foi adicionado na sua pokédex.")
							inspermons[adversario]["hp"] = VidaAdversarioInicial
							break
		
			else:
				luck_inimigo = sorte()
				if luck_inimigo < 1:
					SuasInfo["hp"] = SuasInfo["hp"]
					print ("O ataque do adversário não atingiu você!")
					x += 1
				if luck_inimigo >= 1 and luck < 8:
					SuasInfo["hp"] = SuasInfo["hp"] - (Inimigo["Atk"][1]-SuasInfo["def"])
					print("\n{} usou {}. Foi efetivo!\n".format(Inimigo["nome"],Inimigo["Atk"][0]))
					x += 1
				if luck_inimigo > 7:
					SuasInfo["hp"] = SuasInfo["hp"] - (Inimigo["Atk"][1]+5-SuasInfo["def"])
					print("\n{} usou {}. Foi super efetivo!\n".format(Inimigo["nome"],Inimigo["Atk"][0]))
					x += 1
				if SuasInfo["hp"] <= 0:
					print("\nVocê perdeu a batalha! Seu pokémon desmaiou, reviva ele no PokéCenter")
					SuasInfo["hp"] = 0
					break
					
with open('Insper.json') as arquivo: 
	inspermons = json.load(arquivo)

dados = os.path.isfile('salvadadosauto.dat')
if dados == True:
	continuar=input("Deseja continuar o jogo salvo?\n 	S/N \n")
	if continuar=="S" or continuar =="s":
		with open('salvadadosauto.dat', 'rb') as salvo:
			Insperdex, SuasInfo, xp = pickle.load(salvo)
	else:
		os.remove('salvadadosauto.dat') 
		Inicio = input("--------------------------------------\n  * Qual você escolhe para começar? *\n-------------------------------------- \n 1.Bullbasaur \n 2.Charmander \n 3.Squirtle \n Digite o número: ")
		SuasInfo = inspermons[Inicio]
		print("\nAs suas informações do seu pokemón são:")
		mostra_ipmon(inspermons, Inicio)
		Insperdex = [SuasInfo]
		outros = list(range(1,11))
		xp = 100
else:
	Inicio = input("--------------------------------------\n  * Qual você escolhe para começar? *\n-------------------------------------- \n 1.Bullbasaur \n 2.Charmander \n 3.Squirtle \n Digite o número: ")
	SuasInfo = inspermons[Inicio]
	print("\nAs suas informações do seu pokemón são:")
	mostra_ipmon(inspermons, Inicio)
	Insperdex = [SuasInfo]
	outros = list(range(1,11))
	xp = 100
VidaInicial = SuasInfo["hp"]
outros = list(range(1,11))
	
#Loop principal
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
		Fazer = input("\nO que você quer fazer? \n 1.Passear \n 2.Dormir \n 3.Ir para um PokéCenter\n 4.Voltar \n Digite o número: ")
		print("\n")
		if Fazer == "2":
			print("Até a próxima!")
			break
		if Fazer=="4":
			continue
		elif Fazer == "3":
			print("Bem Vindo ao PokéCenter! Aqui você pode reviver seus pokémons e descobrir mais sobre eles!")
			Desejo = input("Nurse Joy: Oi! Deseja reviver seu pokémon?  S/N ")
			if Desejo == "S" or Desejo == "s":
				SuasInfo["hp"] = VidaInicial
				print("\nA vida do seu pokémon foi restaurada!")
				Desejo2 = input("Nurse Joy: Você deseja entender como funciona a evolução de seus pokémons?")
				if Desejo2 == "S" or Desejo2 == "s":
					print("\n Nurse Joy: A cada batalha que você ganha seu pokémon adquire mais xp, o que faz com que seu ataque fique cada vez mais forte! Espero ter ajudado, e até a próxima!")
				if Desejo2 == "N" or Desejo2 == "n":
					print("\nAté a próxima!")
			if Desejo == "N" or Desejo == "n":
				print("\nVolte sempre!")
	

		elif Fazer == "1" and SuasInfo["hp"] > 0:
			v = batalha(inspermons, outros, SuasInfo, Insperdex, xp)
			if v == "fuga":
				continue
		#elif Fazer == "5":
		#	with open("InsperTrueddd.json", "w") as arquivo: 
		#		json.dump(inspermons, arquivo)
		#	with open("InsperTrue2.json", "w") as arquivo:
		#		json.dump(Insperdex, arquivo)

		else:
			print("Você não pode batalhar com seu Pokémon desmaiado!")
	print("\n**********************************************************\n")
with open('salvadadosauto.dat', 'wb') as salvo:
    pickle.dump([Insperdex, SuasInfo, xp], salvo, protocol=2)