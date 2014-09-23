#!/usr/bin/python3

"""
This is a tiny clone of pokemon.
It may grow, but for now it will be
very, very simple.
"""

from random import randrange

class Bulbasaur():

	name = "Bulbasaur"
	hp = 100
	moves = ["Vine Whip", "Solar Beam", "Tackle", "Growl"]
	mvpwr = [30, 40, 15, 0]
	solar = False

	def attack(self, pokemon, move):
		if self.moves[move] == "Solar Beam" and self.solar:
			print("Bulbasaur needs to recharge.")
			self.solar = False
			return pokemon.hp
		elif self.moves[move] == "Solar Beam" and not self.solar:
			self.solar = True
			return pokemon.hp - self.mvpwr[move]
		else:
			self.solar = False
			return pokemon.hp - self.mvpwr[move]

class Squirtle():

	name = "Squirtle"
	hp = 100
	moves = ["Water Gun", "Hydro Pump", "Tackle", "Splash"]
	mvpwr = [20, 35, 15, 0]

	def attack(self, pokemon, move):
		return pokemon.hp - move

class Game():

	playerPokemon = Bulbasaur()
	oppPokemon = Squirtle()

	def moveSelect(self):
		i = 1
		print("Squirtle: %d"%self.oppPokemon.hp)
		print("Bulbasaur: %d"%self.playerPokemon.hp)
		for move in self.playerPokemon.moves:
			print("%s) %s"%(i,move))
			i += 1
		move = int(input("Which move would you like to use? (choose a corresponding number.) "))
		return move-1

	def logic(self):
		while self.playerPokemon.hp > 0 and self.oppPokemon.hp > 0:
			plmove = self.moveSelect()
			opmove = randrange(1,4)
			print("Squirtle used %s"%self.oppPokemon.moves[opmove])
			self.oppPokemon.hp = self.playerPokemon.attack(self.oppPokemon, plmove)
			self.playerPokemon.hp = self.oppPokemon.attack(self.playerPokemon, self.oppPokemon.mvpwr[opmove])
		if self.playerPokemon.hp <= 0:
			print("Bulbasaur is dead. You lose.")
		elif self.oppPokemon.hp <= 0:
			print("Squirtle is dead. You win.")


def main():
	game = Game()
	game.logic()

if __name__ == "__main__":
	main()
