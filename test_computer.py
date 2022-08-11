from computer import Computer
from pokemon import Pokemon
from pair_pokemon_player import Pair


def test_create_computer_with_non_Computer_name_and_pokemons():
    pokemon = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\
         1, "Fox Pokemon", 1, 1, 1, 1, "", "Delphox", 1, 1, 1, 1, 1, "fire", "psychic", 1, 1, 1)

    player = Computer("Ash", [pokemon])

    assert player.name() == "Computer"
    assert player.pokemons() == [pokemon]


def test_create_computer_with_empty_name_and_pokemons():
    pokemon = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\
         1, "Fox Pokemon", 1, 1, 1, 1, "", "Delphox", 1, 1, 1, 1, 1, "fire", "psychic", 1, 1, 1)

    player = Computer("", [pokemon])

    assert player.name() == "Computer"
    assert player.pokemons() == [pokemon]


def test_set_name_computer_player():
    player = Computer()
    player.set_name()
    assert player.name() == "Computer"


def test_choose_pokemons(monkeypatch):
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\
         1, "Fox Pokemon", 1, 1, 1, 1, "", "Delphox", 1, 1, 1, 1, 1, "fire", "psychic", 1, 1, 1)

    pokemon_2 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\
         1, "Water Pokemon", 1, 1, 1, 1, "", "Eevee", 1, 1, 1, 1, 1, "water", "", 1, 1, 1)

    pokemon_3 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\
         1, "Electric Pokemon", 1, 1, 1, 1, "", "Pikachu", 1, 1, 1, 1, 1, "electricity", "", 1, 1, 1)

    player = Computer()

    def choose_Eevee_and_Pikachu(a, k):
        return [pokemon_2, pokemon_3]

    monkeypatch.setattr("computer.choices", choose_Eevee_and_Pikachu)

    player.choose_pokemons([pokemon_1, pokemon_2, pokemon_3])

    assert player.pokemons() == [pokemon_2, pokemon_3]


def test_choose_fighting_pokemon(monkeypatch):
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\
         1, "Fox Pokemon", 1, 1, 1, 1, "", "Delphox", 1, 1, 1, 1, 1, "fire", "psychic", 1, 1, 1)

    pokemon_2 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\
         1, "Water Pokemon", 1, 1, 1, 1, "", "Eevee", 1, 1, 1, 1, 1, "water", "", 1, 1, 1)

    pokemon_3 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\
         1, "Electric Pokemon", 1, 1, 1, 1, "", "Pikachu", 1, 1, 1, 1, 1, "electricity", "", 1, 1, 1)

    player = Computer("", [pokemon_1, pokemon_2, pokemon_3])

    def choose_eevee(a):
        return pokemon_2

    monkeypatch.setattr("computer.choice", choose_eevee)

    pair = player.choose_fighting_pokemon()

    assert pair == Pair(player, pokemon_2)


def test_choose_your_move():
    pass


def test_choose_new_pokemon(monkeypatch):
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\
         1, "Fox Pokemon", 1, 1, 1, 1, "", "Delphox", 1, 1, 1, 1, 1, "fire", "psychic", 1, 1, 1)

    pokemon_2 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\
         1, "Water Pokemon", 1, 1, 1, 1, "", "Eevee", 1, 1, 1, 1, 1, "water", "", 1, 1, 1)

    pokemon_3 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\
         1, "Electric Pokemon", 1, 1, 1, 1, "", "Pikachu", 1, 1, 1, 1, 1, "electricity", "", 1, 1, 1)

    player = Computer("", [pokemon_1, pokemon_2, pokemon_3])

    def choose_eevee(a):
        return pokemon_2

    monkeypatch.setattr("computer.choice", choose_eevee)

    assert player.choose_new_pokemon([pokemon_2, pokemon_3]) == pokemon_2
