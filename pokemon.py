#!/usr/bin/python3
import os
import shelve
import glob

class Pokemon:						# A class used to represent pokemon and their data.
	def __init__(self, pokeName, pokeNumber):
		self.name = pokeName
		self.number = pokeNumber
	def entry(self, info, weight, height, ptype):
		self.info = info
		self.weight = weight
		self.height = height
		self.ptype = ptype
	def stats(self, attack, defense, health, speed):
		self.attack = attack
		self.defense = defense
		self.health = health
		self.speed = speed




class Pokedex:


	#--------------------------------------------------------------
	#		Init
	#--------------------------------------------------------------
	def __init__(self, name):
		self.name = name	# Named based on the region of the pokedex.


	def access(self, filename):
		pokedexFile = shelve.open("data/%s.pokedex"%filename)
		pokedexFile[filename] = self
		pokedexFile.close()
		print("\n\n\nYou are now in the %s region's pokedex."%self.name)


	#--------------------------------------------------------------
	#		Open a Pokedex
	#--------------------------------------------------------------
	def openDex(self, filename):	# Used to enter into a pokedex in order to access data about its pokemon.
		if os.path.exists("data/%s.pokedex"%filename):			# If the pokedex already exists, open the file for it.
			self.access(filename)
		else:			# If the pokedex does not exist, ask if the user would like to create a new pokedex with the specified name.
			answer = input('The pokedex you specified does not exist yet. Do you want to create it?(y/n) ')
			endloop = 0	# Used for looping to deal with invalid input.
			while endloop!=1:
				if answer=='y':		# Create the pokedex.
					self.access(filename)
					endloop = 1
				elif answer=='n':
					os.chdir("data")
					ls = glob.glob("*.pokedex")
					os.chdir("..")
					if ls:				# List the pokedexes that currently exist.
						files = "  "
						for item in ls:
							files = "%s\n  %s"%(files, item)
						answer = input("Here are the pokedexes that currently exist:\n%s\n\nWould you like to open one of these?(y/n) "%files)
					else:				# If no pokedexes currently exist, do nothing and exit the loop.
						print('\n\n\nPokedex not created.')
						endloop = 1
					while endloop!=1:		# Loop only occurs if pokedexes exist and were listed.
						if answer=='y':
							filename = input('Which one would you like to open?(Enter only the region name) ').capitalize()
							i = 1		# Used to loop only three times so that loop ends if too many invalid entries occur.
							while i<4:
								if not os.path.exists("data/%s.pokedex"%filename):	# Pokedex doesn't exist.
									if i==3:
										print('\n\n\nFile does not exist. Pokedex was not opened.')
										endloop = 1
									else:
										filename = input('File does not exist. Please try again: ')
								else:
									self.access(filename)		# Open the pokedex.
									i = 4
									endloop = 1
								i += 1
						elif answer=='n':
							print('\n\n\nPokedex not created.')
							endloop = 1
						else:
							answer = input('Invalid choice. Please try again:(y/n) ')
				else:
					answer = input('Invalid choice. Please try again:(y/n) ')


	#--------------------------------------------------------------
	#		Make a New Pokedex
	#--------------------------------------------------------------
	def make(self, filename):
		if os.path.exists("data/%s.pokedex"%filename):
			answer = input('Pokedex already exists. Overwrite?(y/n) ')
			endloop = 0
			while endloop!=1:
				if answer=='y':
					os.remove("data/%s.pokedex"%filename)
					self.access(filename)
					endloop = 1
				elif answer=='n':
					print('\n\n\nPokedex not created.')
					endloop = 1
				else:
					answer = input('Invalid choice. Please try again:(y/n) ')
		else:
			self.access(filename)


	#--------------------------------------------------------------
	#		Find a Pokemon
	#--------------------------------------------------------------
	def findPokemon(self, pokeNumber):
		PokemonSearch = Pokemon('unknown', pokeNumber)
		pokeSearch = shelve.open("data/%s.pokedex"%self.name)
		if pokeNumber not in pokeSearch:
			return False
		else:
			PokemonSearch = pokeSearch[pokeNumber]		# Get the object of the pokemon and give it back to the calling function.
			pokeSearch.close()
			return PokemonSearch


	#--------------------------------------------------------------
	#		Make a New Pokemon
	#--------------------------------------------------------------
	def newPokemon(self, PokemonObject, filename):
		pokedexFile = shelve.open("data/%s.pokedex"%filename)
		pokedexFile[PokemonObject.number] = PokemonObject
		pokedexFile.close()




	#--------------------------------------------------------------
	#		Change an Attribute
	#--------------------------------------------------------------
	def changeAttribute(self, name, attribute, values):
		change = input("What would you like to change %s's %s to? "%(name, attribute))
		resp = input('Would you like to change more values?(y/n) ')
		while resp!='n':
			if resp=='y':
				attribute = input("Which value would you like to change? Select from %s: "%values)
				return (change, attribute, 0)
			else:
				resp = input('Invlaid entry. Please try again:(y/n) ')
		return(change, attribute, 1)


	#--------------------------------------------------------------
	#		Change Pokemon Attributes
	#--------------------------------------------------------------
	def changePokemon(self, pokeNumber):
		PokemonChange = Pokemon('unknown', pokeNumber)
		pokeChange = shelve.open("data/%s.pokedex"%self.name)
		if pokeNumber not in pokeChange:
			return False
		else:
			PokemonChange = pokeChange[pokeNumber]
			values = "name, info, weight, height, attack, defense, health, type, speed"
			attribute = input("Which value would you like to change? Select from %s: "%values)
			endloop = 0
			while endloop!=1:
				if attribute=='name':
					value = self.changeAttribute(PokemonChange.name, attribute, values)
					PokemonChange.name = value[0]
					attribute = value[1]
					endloop = value[2]
				elif attribute=='info':
					value = self.changeAttribute(PokemonChange.name, attribute, values)
					PokemonChange.info = value[0]
					attribute = value[1]
					endloop = value[2]
				elif attribute=='weight':
					value = self.changeAttribute(PokemonChange.name, attribute, values)
					PokemonChange.weight = value[0]
					attribute = value[1]
					endloop = value[2]
				elif attribute=='height':
					value = self.changeAttribute(PokemonChange.name, attribute, values)
					PokemonChange.height = value[0]
					attribute = value[1]
					endloop = value[2]
				elif attribute=='attack':
					value = self.changeAttribute(PokemonChange.name, attribute, values)
					PokemonChange.attack = value[0]
					attribute = value[1]
					endloop = value[2]
				elif attribute=='defense':
					value = self.changeAttribute(PokemonChange.name, attribute, values)
					PokemonChange.defense = value[0]
					attribute = value[1]
					endloop = value[2]
				elif attribute=='health':
					value = self.changeAttribute(PokemonChange.name, attribute, values)
					PokemonChange.health = value[0]
					attribute = value[1]
					endloop = value[2]
				elif attribute=='type':
					value = self.changeAttribute(PokemonChange.name, attribute, values)
					PokemonChange.ptype = value[0]
					attribute = value[1]
					endloop = value[2]
				elif attribute=='speed':
					value = self.changeAttribute(PokemonChange.name, attribute, values)
					PokemonChange.speed = value[0]
					attribute = value[1]
					endloop = value[2]
				else:
					attribute = input('Invalid option. Please try again: ')
			pokeChange.close()
			return PokemonChange


	#--------------------------------------------------------------
	#		Remove a Pokemon
	#--------------------------------------------------------------
	def remove(self, pokeNumber):
		PokemonRemove = Pokemon('unknown', pokeNumber)
		pokeRemove = shelve.open("data/%s.pokedex"%self.name)
		pokemon = pokeRemove[pokeNumber].name
		if pokeNumber not in pokeRemove:
			return False
		else:
			del pokeRemove[pokeNumber]
			print("\n\n\n%s removed."%pokemon)
			pokeRemove.close()
			return PokemonRemove


	#--------------------------------------------------------------
	#		Enter Two Types
	#--------------------------------------------------------------
	def dualType(self):
		type1 = input('Enter the first type: ').capitalize()
		type2 = input('Enter the second type: ').capitalize()
		ptype = "%s/%s"%(type1, type2)
		return ptype


	#--------------------------------------------------------------
	#		List All Pokemon
	#--------------------------------------------------------------
	def listAll(self):
		pokelist = "\n  "
		pa = []
		for pokenumber, poke in shelve.open("data/%s.pokedex"%self.name).items():
			if pokenumber != self.name:
				pa.append("%s. %s\n  "%(pokenumber, poke.name))
		pa = sorted(pa)
		for item in pa:
			pokelist = "%s%s"%(pokelist, item)
		print("\n\n\n",pokelist)
