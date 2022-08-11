from pokemon import Pokemon
from pair_pokemon_player import Pair
from human import Human
from os import system
from tabulate import tabulate
from random import choice
import copy
import csv


class Interface():

    def read_from_pokemons(self, handle):
        data = csv.DictReader(handle)
        all_pokemons = []
        for row in data:
            pokemon = Pokemon(
                row["against_bug"],
                row["against_dark"],
                row["against_dragon"],
                row["against_electric"],
                row["against_fairy"],
                row["against_fighting"],
                row["against_fire"],
                row["against_flying"],
                row["against_ghost"],
                row["against_grass"],
                row["against_ground"],
                row["against_ice"],
                row["against_normal"],
                row["against_poison"],
                row["against_psychic"],
                row["against_rock"],
                row["against_steel"],
                row["against_water"],
                row["attack"],
                row["base_egg_steps"],
                row["base_happiness"],
                row["base_total"],
                row["capture_rate"],
                row["classfication"],
                row["defence"],
                row["experience_growth"],
                row["height_m"],
                row["hp"],
                row["japanese_name"],
                row["name"],
                row["percentage_male"],
                row["pokedex_number"],
                row["sp_attack"],
                row["sp_defence"],
                row["speed"],
                row["type1"],
                row["type2"],
                row["weight_kg"],
                row["generation"],
                row["is_legendary"])
            all_pokemons.append(pokemon)
        return all_pokemons

    def choose_game_mode(self):
        system("clear")
        print("Welcome, adventurer!")
        print("Let's begin your thrilling voyage into the world of" +
              " Pokemons.\n")
        print("First thing to do is to choose game mode.")
        print("You have two options:")
        print("1. Fight with your friend")
        print("2. Try yourself out with auto-player\n")

        while True:
            decision = input("What is your choice? Write 1 or 2: ")
            if decision not in ["1", "2"]:
                print("Sorry but you have to write either 1 or 2.")
                continue
            else:
                return decision

    def get_players_names(self, mode):
        system('clear')
        order_words = ["First", "Second"]
        counter = 0
        names = []
        print(f"{order_words[counter]} player!")
        self.get_individual_name(names, mode)
        counter += 1
        if mode == "1":
            print(f"{order_words[counter]} player!")
            self.get_individual_name(names, mode)

        return names

    def chceck_if_not_correct_name(self, name, names, mode):
        if not name:
            print("You can't have an empty name. Try again.\n")
            return True

        if name in names:
            print("Players need to have different names." +
                  " Choose another name.\n")
            return True

        if name == "Computer" and mode == "2":
            print("This name is already reserved for auto-player." +
                  " Try another name.\n")
            return True

        else:
            return False

    def get_individual_name(self, names, mode):
        name_is_not_ok = True
        while name_is_not_ok:
            name = input("What's your name? ")
            name_is_not_ok = self.chceck_if_not_correct_name(name, names, mode)
            if not name_is_not_ok:
                names.append(name)
                system('clear')

    def choose_pokemons(self, pokemons, player):
        all_pokemons_names = [pokemon.name() for pokemon in pokemons]
        chosen_pokemons = []
        chosen_pokemons_names = []
        number_of_pokemons = 0
        print(f"{player.name()}, choose your Pokemons!")
        print("Available pokemons:\n")
        print(self.format_pokemons_names(pokemons))
        print("\nChoose your pokemons writing their names and pressing ENTER.")
        print("Remember that you can have from 1 to 6 pokemons in your team.")
        print("When you want to choose less than 6 pokemons, press ENTER" +
              " after displaying next row to stop choosing.")

        while True:
            if number_of_pokemons == 6:
                print("\n")
                break

            decision = input(f"{number_of_pokemons + 1}. ")

            if not decision:
                if number_of_pokemons == 0:
                    print("You need to have at least one pokemon in your team")
                    continue

                else:
                    print("\n")
                    break

            else:
                if decision in all_pokemons_names:
                    pokemon = self.get_pokemon_by_name(pokemons, decision)
                    pokemon = copy.copy(pokemon)
                    if not pokemon.name() in chosen_pokemons_names:
                        chosen_pokemons.append(pokemon)
                        chosen_pokemons_names.append(pokemon.name())
                        number_of_pokemons += 1
                    else:
                        print("You can't choose twice the same Pokemon")
                        continue

                else:
                    print("Sorry, but there is no such a pokemon. Maybe you" +
                          " wrote his name wrong? Try again.")
                    continue
        system("clear")
        return chosen_pokemons

    def get_pokemon_by_name(self, pokemons, name):
        for pokemon in pokemons:
            if pokemon.name() == name:
                return pokemon

        return None

    def format_pokemons_names(self, pokemons):
        rows = self.create_list_of_rows(pokemons)
        return tabulate(rows,
                        headers=["Pokemon name",
                                 "Hp",
                                 "Speed",
                                 "Attack",
                                 "Special attack",
                                 "Defence",
                                 "Special defence"],
                        tablefmt="presto")

    def create_list_of_rows(self, pokemons):
        pokemons_names = [pokemon.name() for pokemon in pokemons]
        pokemons_hp = [pokemon.hp() for pokemon in pokemons]
        pokemons_speed = [pokemon.speed() for pokemon in pokemons]
        pokemons_attack = [pokemon.attack() for pokemon in pokemons]
        pokemons_sp_attack = [pokemon.sp_attack() for pokemon in pokemons]
        pokemons_defence = [pokemon.defence() for pokemon in pokemons]
        pokemons_sp_defence = [pokemon.sp_defence() for pokemon in pokemons]
        rows = []
        for (name,
             hp,
             speed,
             attack,
             sp_attack,
             defence,
             sp_defence) in zip(pokemons_names,
                                pokemons_hp,
                                pokemons_speed,
                                pokemons_attack,
                                pokemons_sp_attack,
                                pokemons_defence,
                                pokemons_sp_defence):
            rows.append(
                    [name, hp, speed, attack, sp_attack, defence, sp_defence]
                    )

        return rows

    def prepare_for_battle(self, players):
        pairs = []
        for player in players:
            print("-------------------------")
            print("Let's prepare for battles!")
            print("-------------------------\n")
            if isinstance(player, Human):
                pair = self.choose_fighting_pokemon(player)
            else:
                pokemon = choice(player.pokemons())
                pair = Pair(player, pokemon)
            pairs.append(pair)
            system("clear")
        return pairs

    def choose_fighting_pokemon(self, player):
        pokemons = player.pokemons()
        print(f"{player.name()} choose your first Pokemon.")
        print("Here's a list of your Pokemons\n")
        print(self.format_pokemons_names(pokemons))
        if len(pokemons) == 1:
            pokemon = pokemons[0]
            print(f"\n I choose: {pokemon.name()}")

        else:
            while True:
                pokemon = input("\nI choose: ")
                if pokemon in player.pokemons_names():
                    pokemon = self.get_pokemon_by_name(pokemons, pokemon)
                    break

                else:
                    print("Sorry but there is no such a Pokemon in your team."
                          + " Maybe you made a typo. Try again")
                    continue
        pair = Pair(player, pokemon)
        return pair

    def begin_clash(self):
        print('Time to start the battle!\n')
        input()
        system("clear")

    def team_description(self, round_n, pairs):
        print(f"{round_n}. round")
        print("\n-------------------------\n")
        for pair in pairs:
            player_name = pair.player().name()
            chosen_pokemon_name = pair.pokemon().name()
            print(f"{player_name} fights with {chosen_pokemon_name}\n")
        input()
        system("clear")

    def choose_your_move(self, player, enemy, chosen_pokemon):
        print(f"{player.name()}, choose your move! Write the digit of your" +
              " choice\n")
        print("1. Defence")
        print("2. Normal attack")
        print("3. Special attack")
        print("4. Switch Pokemon\n")
        print(f"Your Pokemon: {chosen_pokemon.name()} - stats:\n")
        print(self.basic_stats_table(chosen_pokemon))
        print("\n")
        print(f"\nEnemie's Pokemon {enemy.pokemon().name()} - stats:\n")
        print(self.basic_stats_table(enemy.pokemon()))
        print("\n")
        while True:
            decision = input("My move: ")
            if decision not in ["1", "2", "3", "4"]:
                print("You should write 1, 2, 3 or 4")
                continue
            else:
                if len(player.pokemons()) == 1 and decision == "4":
                    print("You have only 1 Pokemon so you can`t change it." +
                          "Choose another move.")
                    continue

                else:
                    break

        system("clear")
        return decision

    def basic_stats_table(self, pokemon):
        basic_headers = ["Hp",
                         "Attack",
                         "Special attack",
                         "Defence",
                         "Special defence"]
        table = tabulate(
            [pokemon.basic_stats()],
            headers=basic_headers,
            tablefmt="presto")
        return table

    def announce_end_of_pokemons(self, pair):
        player = pair.player()
        print(f"{player.name()}, you lost your last Pokemon.")

    def announce_player_turn(self, pair):
        player_name = pair.player().name()
        print(f"{player_name}'s' move.\n")

    def wait_for_enter(self):
        input()
        system('clear')

    def defence_change_description(self, pokemon):
        print(f"{pokemon.name()}'s defence increased by 10%.")
        print(f"Current defence: {pokemon.defence()}")

    def information_about_damage(self, pair, damage):
        enemy_pokemon = pair.enemy().pokemon()
        info = f"{pair.pokemon()} attacked {enemy_pokemon}. {enemy_pokemon}"
        info += f" took {damage} damage."
        print(info)

    def choose_attack_type(self, pokemon):
        print("Choose type of your special attack.")
        print(f"1. {pokemon.type1()}")
        print(f"2. {pokemon.type2()}\n")
        print("Write number of your choice.")

        while True:
            decision = input("My choice: ")
            if decision == "1":
                return pokemon.type1()

            elif decision == "2":
                return pokemon.type2()

            else:
                print("Sorry but you have to write either 1 or 2.")
                continue

    def new_pokemon_needed(self, pair):
        print(f"{pair.player().name()}, your Pokemon lost all hp.")
        print("You have to choose new Pokemon for the next round.\n")

    def choose_new_pokemon(self, other_pokemons, current_pokemon, mode):
        other_pokemons_names = [pokemon.name() for pokemon in other_pokemons]
        print("Choose pokemon that you want to fight with!\n")
        print("Available pokemons:\n")
        print(self.format_pokemons_names(other_pokemons)+"\n\n")
        if mode == "1":
            print("Pokemon that your'are currently fighting with:\n")
            print(self.format_pokemons_names([current_pokemon]) + "\n")
        while True:
            pokemon = input("I choose: ")
            if pokemon in other_pokemons_names:
                pokemon = self.get_pokemon_by_name(other_pokemons, pokemon)
                return pokemon
            else:
                print("Sorry but there is no such a Pokemon in your team." +
                      " Maybe you made a typo. Try again")
                continue

    def switched_pokemons_info(self, current_pokemon_name, new_pokemon):
        print(f"{current_pokemon_name} switched with {new_pokemon.name()}.")

    def last_pokemon_info(self, new_pokemon):
        print("You have only one Pokemon left so you are going to fight" +
              f" with - {new_pokemon.name()}.")

    def one_more_pokemon_in_team_info(self, new_pokemon):
        print("You have only one more Pokemon in your team so you are going" +
              f" to fight with - {new_pokemon.name()}.")

    def annouce_winner(self, winner):
        print(f"The winner is {winner.name()}!")

    def clear_terminal(self):
        system('clear')
