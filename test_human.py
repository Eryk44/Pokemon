from human import Human
from pokemon import Pokemon


def test_create_human_with_name_and_pokemons():
    pokemon = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, "Fox Pokemon", 1, 1, 1, 1, "", "Delphox", 1,
                      1, 1, 1, 1, "fire", "psychic", 1, 1, 1)

    player = Human("Ash", [pokemon])

    assert player.name() == "Ash"
    assert player.pokemons() == [pokemon]


def test_create_human_with_no_name_and_no_pokemons():
    player = Human()

    assert player.name() == ""
    assert player.pokemons() == ""


def test_set_player_name():
    player = Human()

    player.set_name("Ash")

    assert player.name() == "Ash"
