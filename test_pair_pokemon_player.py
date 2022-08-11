from pair_pokemon_player import Pair
from player import Player
from human import Human
from computer import Computer
from pokemon import Pokemon


def test_create_pair():
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, "Fox Pokemon", 1, 1, 1, 1, "",
                        "Delphox", 1, 1, 1, 1, 1, "fire", "psychic", 1, 1, 1)

    pokemon_2 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, "Water Pokemon", 1, 1, 1, 1, "",
                        "Eevee", 1, 1, 1, 1, 1, "water", "", 1, 1, 1)

    player = Player("Ash", [pokemon_1, pokemon_2])

    pair = Pair(player, pokemon_1)

    assert pair.player() == player
    assert pair.pokemon() == pokemon_1
    assert pair.miss_turn() is False


def test_set_enemy():
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, "Fox Pokemon", 1, 1, 1, 1, "",
                        "Delphox", 1, 1, 1, 1, 1, "fire", "psychic", 1, 1, 1)

    pokemon_2 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, "Water Pokemon", 1, 1, 1, 1, "",
                        "Eevee", 1, 1, 1, 1, 1, "water", "", 1, 1, 1)

    player_1 = Player("Ash", [pokemon_1])
    player_2 = Player("James", [pokemon_2])

    pair_1 = Pair(player_1, pokemon_1)
    pair_2 = Pair(player_2, pokemon_2)

    pair_1.set_enemy([pair_1, pair_2])

    assert pair_1.enemy() == pair_2


def test_set_miss_turn():
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, "Fox Pokemon", 1, 1, 1, 1, "",
                        "Delphox", 1, 1, 1, 1, 1, "fire", "psychic", 1, 1, 1)

    pokemon_2 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, "Water Pokemon", 1, 1, 1, 1, "",
                        "Eevee", 1, 1, 1, 1, 1, "water", "", 1, 1, 1)

    player_1 = Player("Ash", [pokemon_1, pokemon_2])
    pair_1 = Pair(player_1, pokemon_1)

    assert pair_1.miss_turn() is False

    pair_1.set_miss_turn(True)

    assert pair_1.miss_turn() is True


def test_change_pokemon():
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, "Fox Pokemon", 1, 1, 1, 1, "",
                        "Delphox", 1, 1, 1, 1, 1, "fire", "psychic", 1, 1, 1)

    pokemon_2 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, "Water Pokemon", 1, 1, 1, 1, "",
                        "Eevee", 1, 1, 1, 1, 1, "water", "", 1, 1, 1)

    pokemon_3 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, "Electric Pokemon", 1, 1, 1, 1, "",
                        "Pikachu", 1, 1, 1, 1, 1, "electricity", "", 1, 1, 1)

    player = Human("Ash", [pokemon_1, pokemon_2, pokemon_3])
    pair = Pair(player, pokemon_1)

    pair.change_pokemon(pokemon_3)

    assert pair.pokemon() == pokemon_3


def test_defence():
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, "Fox Pokemon", 20, 1, 1, 1, "",
                        "Delphox", 1, 1, 1, 1, 1, "fire", "psychic", 1, 1, 1)

    player = Human("Ash", [pokemon_1])
    pair = Pair(player, pokemon_1)

    pair.defence()

    assert pokemon_1.defence() == 22


def test_attack(monkeypatch):
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        10, 1, 1, 1, 1, "Fox Pokemon", 1, 1, 1, 1, "",
                        "Delphox", 1, 1, 1, 1, 1, "fire", "psychic", 1, 1, 1)

    pokemon_2 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, "Water Pokemon", 10, 1, 1, 50, "",
                        "Eevee", 1, 1, 1, 1, 1, "water", "", 1, 1, 1)

    player_1 = Player("Ash", [pokemon_1])
    player_2 = Player("James", [pokemon_2])

    pair_1 = Pair(player_1, pokemon_1)
    pair_2 = Pair(player_2, pokemon_2)

    pair_1.set_enemy([pair_1, pair_2])

    def give_one(a, b):
        return 1

    monkeypatch.setattr("pair_pokemon_player.uniform", give_one)

    pair_1.attack()

    assert pokemon_2.hp() == 45


def test_special_attack(monkeypatch):
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        10, 1, 1, 1, 1, "Fox Pokemon", 1, 1, 1, 1, "",
                        "Delphox", 1, 1, 20, 1, 1, "fire", "psychic", 1, 1, 1)

    pokemon_2 = Pokemon(0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, "Water Pokemon", 10, 1, 1, 50, "",
                        "Eevee", 1, 1, 1, 10, 1, "water", "", 1, 1, 1)

    player_1 = Player("Ash", [pokemon_1])
    player_2 = Player("James", [pokemon_2])

    pair_1 = Pair(player_1, pokemon_1)
    pair_2 = Pair(player_2, pokemon_2)

    pair_1.set_enemy([pair_1, pair_2])

    def give_one(a, b):
        return 1

    monkeypatch.setattr("pair_pokemon_player.uniform", give_one)

    pair_1.special_attack("bug")

    assert pokemon_2.hp() == 46


def test_attack_enemy_pokemon_no_kill():
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        10, 1, 1, 1, 1, "Fox Pokemon", 1, 1, 1, 1, "",
                        "Delphox", 1, 1, 20, 1, 1, "fire", "psychic", 1, 1, 1)

    pokemon_2 = Pokemon(0.5, 0.25, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, 1, "Water Pokemon", 10, 1, 1, 50, "",
                        "Eevee", 1, 1, 1, 10, 1, "water", "", 1, 1, 1)

    player_1 = Computer("", [pokemon_1])
    player_2 = Player("James", [pokemon_2])

    pair_1 = Pair(player_1, pokemon_1)
    pair_2 = Pair(player_2, pokemon_2)

    pair_1.attack_enemy_pokemon(24, pokemon_2, pair_2)

    assert pokemon_2.hp() == 26


def test_attack_enemy_pokemon_with_kill():
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        10, 1, 1, 1, 1, "Fox Pokemon", 1, 1, 1, 1, "",
                        "Delphox", 1, 1, 20, 1, 1, "fire", "psychic", 1, 1, 1)

    pokemon_2 = Pokemon(0.5, 0.25, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, 1, "Water Pokemon", 10, 1, 1, 50, "",
                        "Eevee", 1, 1, 1, 10, 1, "water", "", 1, 1, 1)

    player_1 = Computer("", [pokemon_1])
    player_2 = Player("James", [pokemon_2])

    pair_1 = Pair(player_1, pokemon_1)
    pair_2 = Pair(player_2, pokemon_2)

    pair_1.attack_enemy_pokemon(60, pokemon_2, pair_2)

    assert player_2.pokemons() == []
    assert pair_2.miss_turn() is True
