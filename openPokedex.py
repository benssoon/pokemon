#!/usr/bin/python3
import pokemon

def getChoice(menu):
        print(menu)
        choice = int(input('What would you like to do?\nEnter a number: '))
        return choice
menu = '''
	1) Open a pokedex
	2) Create a pokedex
	3) Enter newly discovered pokemon
	4) Change a pokedex entry
	5) Get pokedex entry
	6) Get pokemon stats
	7) List all pokemon in the pokedex
	8) Remove a pokemon
	9) Quit
'''
MyPokedex = ""
choice = getChoice(menu)
while choice!=9:
	#----------------------------------------------------------------------------------
	#		Open a pokedex from a certain region.
	#----------------------------------------------------------------------------------
	if choice==1:
		regionName = input('Enter the name of the region whose pokedex you wish to see: ').capitalize()
		MyPokedex = pokemon.Pokedex(regionName)
		MyPokedex.openDex(regionName)


	#----------------------------------------------------------------------------------
	#		Create a new pokedex.
	#----------------------------------------------------------------------------------
	elif choice==2:		
		regionName = input('Enter the name of the region whose pokedex you wish to create: ').capitalize()
		MyPokedex = pokemon.Pokedex(regionName)
		MyPokedex.make(regionName)


	#----------------------------------------------------------------------------------
	#		Enter a new pokemon into the current pokedex.
	#----------------------------------------------------------------------------------
	elif choice==3:		
		if MyPokedex=="":
			print("Open a pokedex first.")
		else:
			discoverPokemon = input('Enter the name of the pokemon you just discovered and its number, separated by a space: ')
			discoverPokemon = discoverPokemon.split()
			name = discoverPokemon[0].capitalize()
			number = discoverPokemon[1]
			DiscoveredPokemon = pokemon.Pokemon(name, number)
			ptype = input('Enter the type of the pokemon(type "dual" for a dual-type pokemon): ').capitalize()
			if ptype=='Dual':
				ptype = MyPokedex.dualType()
			height = float(input('Enter the height of the pokemon: '))
			weight = float(input('Enter the weight of the pokemon: '))
			info = input('Enter one or two sentences that give some information about the pokemon: ').capitalize()
			health = int(input('Enter the health of the pokemon: '))
			attack = int(input('Enter the attack of the pokemon: '))
			defense = int(input('Enter the defense of the pokemon: '))
			speed = int(input('Enter the speed of the pokemon: '))
			DiscoveredPokemon.entry(info, weight, height, ptype)
			DiscoveredPokemon.stats(attack, defense, health, speed)
			MyPokedex.newPokemon(DiscoveredPokemon, MyPokedex.name)


	#----------------------------------------------------------------------------------
	#		Change data from an existing pokemon in the current pokedex.
	#----------------------------------------------------------------------------------
	elif choice==4:		
		if MyPokedex=="":
			print("Open a pokedex first.")
		else:
			pokeNumber = input('Enter the number of the pokemon whose data you wish to change: ')
			if MyPokedex.findPokemon(pokeNumber)==False:
				print("There is currently no pokemon assigned to entry number %s. Please select option 3 if you wish to create it."%pokeNumber)
			else:
				ChangedPokemon = MyPokedex.changePokemon(pokeNumber)
				MyPokedex.newPokemon(ChangedPokemon, MyPokedex.name)


	#----------------------------------------------------------------------------------
	#		Get basic pokedex data for a specified pokemon.
	#----------------------------------------------------------------------------------
	elif choice==5:		
		if MyPokedex=="":
			print("Open a pokedex first.")
		else:
			pokeNumber = input('Enter the number of the pokemon you wish to look up: ')
			if MyPokedex.findPokemon(pokeNumber)==False:
				print("There is currently no pokemon assigned to entry number %s. Please select option 3 if you wish to create it."%pokeNumber)
			else:
				TempPoke = MyPokedex.findPokemon(pokeNumber)
				name = TempPoke.name
				ptype = TempPoke.ptype
				info = TempPoke.info
				weight = TempPoke.weight
				height = TempPoke.height
				height = "%s'%s\""%(str(height).split('.')[0], str(height).split('.')[1])
				spacestr = ' '*5
				dashstr = '-'*len(TempPoke.name)
				print("%s%s\n%s%s\nAbout: %s\nType: %s\nWeight: %.1f lbs\nHeight: %s"%(spacestr, name, spacestr, dashstr, info, ptype, weight, height))


	#----------------------------------------------------------------------------------
	#		Get battle related data for a specified pokemon.
	#----------------------------------------------------------------------------------
	elif choice==6:		
		if MyPokedex=="":
			print("Open a pokedex first.")
		else:
			pokeNumber = input('Enter the number of the pokemon you wish to look up: ')
			if MyPokedex.findPokemon(pokeNumber)==False:
				print("There is currently no pokemon assigned to entry number %s. Please select option 3 if you wish to create it."%pokeNumber)
			else:
				TempPoke = MyPokedex.findPokemon(pokeNumber)
				name = TempPoke.name
				health = TempPoke.health
				attack = TempPoke.attack
				defense = TempPoke.defense
				speed = TempPoke.speed
				spacestr = ' '*5
				dashstr = '-'*len(TempPoke.name)
				print("%s%s\n%s%s\nHealth: %s\nAttack: %d\nDefense: %d\nSpeed: %d"%(spacestr, name, spacestr, dashstr, health, attack, defense, speed))


	#----------------------------------------------------------------------------------
	#		List all of the pokemon in the current pokedex.
	#----------------------------------------------------------------------------------
	elif choice==7:		
		if MyPokedex=="":
			print("Open a pokedex first.")
		else:
			MyPokedex.listAll()


	#----------------------------------------------------------------------------------
	#		Delete a pokemon
	#----------------------------------------------------------------------------------
	elif choice==8:
		if MyPokedex=="":
			print("Open a pokedex first.")
		else:
			pokemon = input("Enter the number of the pokemon you would like to remove: ")
			del MyPokedex[pokemon]
	else:
		print('Invalid choice, please try again.')
	choice = getChoice(menu)
print("Goodbye")
