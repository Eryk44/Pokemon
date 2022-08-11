from interface import Interface
from game import Game
from human import Human
from computer import Computer
from battle_ground import BattleGround
from random import sample, choice


class Controller:

    def __init__(self):
        self._interface = Interface()

    def interface(self):
        return self._interface

    def game(self):
        return self._game

    def battle_ground(self):
        return self._battle_ground

    def conduct_game(self):
        pokemons = self.prepare_pokemons()
        self.create_game(pokemons)
        game_mode = self.choose_game_mode()
        self.set_game_mode(game_mode)
        self.create_players()
        self.set_players_names()
        self.set_players_pokemons(pokemons)
        pairs = self.prepare_battle_ground()
        self.create_battle_ground(pairs)
        self.control_battle_ground()

    def create_battle_ground(self, pairs):
        self._battle_ground = BattleGround(pairs)

    def control_battle_ground(self):
        self.interface().begin_clash()
        battle_ground = self.battle_ground()
        pairs = battle_ground.pairs()
        players = [pair.player() for pair in pairs]
        all_players_pokemons = [player.pokemons() for player in players]
        round_n = 1
        while all_players_pokemons[0] and all_players_pokemons[1]:
            self.interface().team_description(round_n, pairs)
            self.round()
            round_n += 1
        self.interface().wait_for_enter()
        winner = battle_ground.winner()
        self.interface().annouce_winner(winner)

    def round(self):
        battle_ground = self.battle_ground()
        pairs = battle_ground.pairs()
        self.get_players_move(pairs)

        ordered_pairs = battle_ground.speed_comparison()

        for pair in ordered_pairs:
            if pair.miss_turn():
                self.ask_for_change_of_dead_pokemon(pair)

            else:
                self.interface().announce_player_turn(pair)
                self.control_pair_move(pair)
                self.interface().wait_for_enter()

        first_pair = ordered_pairs[0]
        if first_pair.miss_turn():
            self.ask_for_change_of_dead_pokemon(first_pair)

    def ask_for_change_of_dead_pokemon(self, pair):
        if pair.player().pokemons():
            self.interface().new_pokemon_needed(pair)
            self.change_dead_pokemon(pair, "2")
            if len(pair.player().pokemons()) == 1:
                self.interface().last_pokemon_info(pair.pokemon())
            if isinstance(pair.player(), Human):
                self.interface().wait_for_enter()
            else:
                self.interface().clear_terminal()

        else:
            self.interface().announce_end_of_pokemons(pair)

        pair.set_miss_turn(False)

    def control_pair_move(self, pair):
        decision = pair.move()
        interface = self.interface()

        if decision == "1":
            pair.defence()
            interface.defence_change_description(pair.pokemon())

        elif decision == "2":
            damage = pair.attack()
            interface.information_about_damage(pair, damage)

        elif decision == "3":
            chosen_type = self.choose_pokemon_type(pair)
            damage = pair.special_attack(chosen_type)
            interface.information_about_damage(pair, damage)

        elif decision == "4":
            new_pokemon = self.choose_pokemon_to_swich(pair)
            pair.change_pokemon(new_pokemon)

    def choose_pokemon_type(self, pair):
        pokemon = pair.pokemon()
        player = pair.player()
        if not pokemon.type2():
            chosen_type = pokemon.type1()

        else:
            if isinstance(player, Computer):
                chosen_type = choice(pokemon.type1(), pokemon.type2())

            else:
                chosen_type = self.interface().choose_attack_type(pokemon)
        return chosen_type

    def get_players_move(self, pairs):
        for pair in pairs:
            pair.set_enemy(pairs)
            player = pair.player()
            if isinstance(player, Human):
                decision = self.interface().choose_your_move(player,
                                                             pair.enemy(),
                                                             pair.pokemon())
            else:
                decision = player.choose_your_move(pair.enemy(),
                                                   pair.pokemon())
            pair.current_move(decision)

    def change_dead_pokemon(self, pair, mode):
        new_pokemon = self.choose_pokemon_to_swich(pair, mode)
        pair.change_pokemon(new_pokemon)

    def choose_pokemon_to_swich(self, pair, mode="1"):
        player = pair.player()
        player_pokemons = player.pokemons()
        current_pokemon = pair.pokemon()
        current_pokemon_name = current_pokemon.name()
        other_pokemons = self.player_pokemons_not_in_pair(player_pokemons,
                                                          current_pokemon_name)
        if len(player_pokemons) == 2:
            new_pokemon = other_pokemons[0]
            self.interface().one_more_pokemon_in_team_info(new_pokemon)

        elif len(other_pokemons) == 1:
            new_pokemon = other_pokemons[0]

        elif isinstance(player, Computer):
            new_pokemon = player.choose_new_pokemon(other_pokemons)
            return new_pokemon

        else:
            new_pokemon = self.interface().choose_new_pokemon(other_pokemons,
                                                              current_pokemon,
                                                              mode)
            self.interface().switched_pokemons_info(current_pokemon_name,
                                                    new_pokemon)

        return new_pokemon

    def player_pokemons_not_in_pair(self, player_pokemons,
                                    current_pokemon_name):
        other_pokemons = []
        for pokemon in player_pokemons:
            if pokemon.name() == current_pokemon_name:
                continue
            else:
                other_pokemons.append(pokemon)
        return other_pokemons

    def prepare_pokemons(self, number=20, handle='pokemon.csv'):
        with open(handle, mode='r') as handle:
            pokemons = self.interface().read_from_pokemons(handle)
        return sample(pokemons, k=number)

    def create_game(self, pokemons):
        game = Game(pokemons)
        self._game = game
        return game

    def choose_game_mode(self):
        decision = self.interface().choose_game_mode()
        return decision

    def set_game_mode(self, mode):
        game = self.game()
        game.set_game_mode(mode)

    def create_players(self):
        game = self.game()
        game.set_players()

    def set_players_names(self):
        game = self.game()
        game_mode = game.mode()
        names = self.interface().get_players_names(game_mode)
        game.set_players_names(names)

    def set_players_pokemons(self, pokemons):
        game = self.game()
        players = game.players()
        for player in players:
            if isinstance(player, Human):
                chosen_pokemons = self.interface().choose_pokemons(pokemons,
                                                                   player)
                player.set_pokemons(chosen_pokemons)
            else:
                player.choose_pokemons(pokemons)

    def prepare_battle_ground(self):
        game = self.game()
        players = game.players()
        return self.interface().prepare_for_battle(players)
