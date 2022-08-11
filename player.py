class Player():
    def __init__(self, name="", pokemons=""):
        self._name = name
        self._pokemons = pokemons

    def name(self):
        return self._name

    def pokemons(self):
        return self._pokemons

    def pokemons_names(self):
        pokemon_names = [pokemon.name() for pokemon in self.pokemons()]
        return pokemon_names

    def remove_pokemon(self, pokemon):
        self._pokemons.remove(pokemon)
