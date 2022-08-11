from battle_ground import BattleGround
from human import Human
from pokemon import Pokemon
from pair_pokemon_player import Pair


def test_create_battle_ground():
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        10, 1, 1, 1, 1, "Fox Pokemon", 70, 1, 1, 40, "",
                        "Delphox", 1, 1, 20, 50, 30, "dark", "bug", 1, 1, 1)

    pokemon_2 = Pokemon(0.5, 0.25, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 100, 1, 1, 1, 1, "Water Pokemon", 15, 1, 1, 50,
                        "", "Eevee", 1, 1, 1, 10, 60, "water", "", 1, 1, 1)

    player_1 = Human("Ash", [pokemon_1, pokemon_2])
    player_2 = Human("James", [pokemon_2])

    pair_1 = Pair(player_1, pokemon_1)
    pair_2 = Pair(player_2, pokemon_2)

    battle_ground = BattleGround([pair_1, pair_2])

    assert battle_ground.pairs()[0] == pair_1
    assert battle_ground.pairs()[1] == pair_2


def test_speed_comparison():
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 10, 1, 1, 1, 1, "Fox Pokemon", 70, 1, 1, 40, "",
                        "Delphox", 1, 1, 20, 50, 30, "dark", "bug", 1, 1, 1)

    pokemon_2 = Pokemon(0.5, 0.25, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 100, 1, 1, 1, 1, "Water Pokemon", 15, 1, 1, 50,
                        "", "Eevee", 1, 1, 1, 10, 60, "water", "", 1, 1, 1)

    player_1 = Human("Ash", [pokemon_1, pokemon_2])
    player_2 = Human("James", [pokemon_2])

    pair_1 = Pair(player_1, pokemon_1)
    pair_2 = Pair(player_2, pokemon_2)

    battle_ground = BattleGround([pair_1, pair_2])

    assert battle_ground.speed_comparison() == [pair_2, pair_1]


def test_winner():
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        10, 1, 1, 1, 1, "Fox Pokemon", 70, 1, 1, 40, "",
                        "Delphox", 1, 1, 20, 50, 30, "dark", "bug", 1, 1, 1)

    pokemon_2 = Pokemon(0.5, 0.25, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 100, 1, 1, 1, 1, "Water Pokemon", 15, 1, 1, 50, "",
                        "Eevee", 1, 1, 1, 10, 60, "water", "", 1, 1, 1)

    player_1 = Human("Ash", [pokemon_1, pokemon_2])
    player_2 = Human("James", [])

    pair_1 = Pair(player_1, pokemon_1)
    pair_2 = Pair(player_2, pokemon_2)

    battle_ground = BattleGround([pair_1, pair_2])

    assert battle_ground.winner() == player_1
