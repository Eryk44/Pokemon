from player import Player
from pair_pokemon_player import Pair
from random import randint, choices, choice


class Computer(Player):
    def __init__(self, name="", pokemons=""):
        super().__init__("Computer", pokemons)

    def set_name(self):
        self._name = "Computer"

    def choose_pokemons(self, pokemons, min_pokemons=1, max_pokemons=6):
        number_of_pokemons = randint(min_pokemons, max_pokemons)
        chosen_pokemons = choices(pokemons, k=number_of_pokemons)
        self._pokemons = chosen_pokemons

    def choose_fighting_pokemon(self):
        pokemon = choice(self.pokemons())
        pair = Pair(self, pokemon)
        return pair

    def choose_your_move(self, enemy, chosen_pokemon, number=10):
        enemy_pokemon = enemy.pokemon()
        if chosen_pokemon.hp() - number > enemy_pokemon.hp():
            return "1"

        elif enemy_pokemon.hp() <= 0.8 * chosen_pokemon.hp():
            return "2"

        elif enemy_pokemon.hp() <= chosen_pokemon.hp()/8:
            return "3"

        elif chosen_pokemon.hp() < number:
            if not self.pokemons():
                return "4"

            else:
                return "2"

        else:
            return "2"

    def choose_new_pokemon(self, other_pokemons, current_pokemon=""):
        return choice(other_pokemons)
