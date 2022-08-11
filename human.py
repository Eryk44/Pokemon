from player import Player


class Human(Player):

    def __init__(self, name="", pokemons=""):
        super().__init__(name, pokemons)

    def set_name(self, name):
        self._name = name

    def set_pokemons(self, chosen_pokemons):
        self._pokemons = chosen_pokemons
