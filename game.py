from human import Human
from computer import Computer


class Game:
    def __init__(self, pokemons=None, players=None):
        self._pokemons = pokemons
        self._players = players

    def pokemons(self):
        return self._pokemons

    def players(self):
        return self._players

    def mode(self):
        return self._mode

    def set_game_mode(self, mode):
        self._mode = mode

    def set_players(self):
        mode = self.mode()
        players = [Human()]
        if mode == "1":
            players.append(Human())

        else:
            players.append(Computer())

        self._players = players

    def set_players_names(self, names):
        mode = self.mode()
        players = self.players()
        if mode == "1":
            for name, player in zip(names, players):
                player.set_name(name)

        if mode == "2":
            for player in players:
                if isinstance(player, Human):
                    player.set_name(names[0])
