from game import Game
from pokemon import Pokemon
from human import Human
from computer import Computer
from player import Player


def test_create_game_with_pokemons():
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        10, 1, 1, 1, 1, "Fox Pokemon", 70, 1, 1, 40, "",
                        "Delphox", 1, 1, 20, 50, 30, "dark", "bug", 1, 1, 1)

    pokemon_2 = Pokemon(0.5, 0.25, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 100, 1, 1, 1, 1, "Water Pokemon", 15, 1,
                        1, 50, "", "Eevee", 1, 1, 1, 10, 60, "water", "",
                        1, 1, 1)

    game = Game([pokemon_1, pokemon_2])

    assert game.pokemons() == [pokemon_1, pokemon_2]
    assert game.players() is None


def test_create_game_without_pokemons():
    game = Game()

    assert game.pokemons() is None
    assert game.players() is None


def test_set_game_mode():
    game = Game()

    game.set_game_mode("1")
    assert game.mode() == "1"


def test_create_game_with_players():
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        10, 1, 1, 1, 1, "Fox Pokemon", 70, 1, 1, 40, "",
                        "Delphox", 1, 1, 20, 50, 30, "dark", "bug", 1, 1, 1)

    pokemon_2 = Pokemon(0.5, 0.25, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 100, 1, 1, 1, 1, "Water Pokemon", 15, 1,
                        1, 50, "", "Eevee", 1, 1, 1, 10, 60, "water", "",
                        1, 1, 1)

    player_1 = Player("Ash", [pokemon_1])
    player_2 = Player("James", [pokemon_2])

    game = Game([pokemon_1, pokemon_2], [player_1, player_2])

    assert game.pokemons() == [pokemon_1, pokemon_2]
    assert game.players() == [player_1, player_2]


def test_set_players_game_with_two_humans():
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        10, 1, 1, 1, 1, "Fox Pokemon", 70, 1, 1, 40, "",
                        "Delphox", 1, 1, 20, 50, 30, "dark", "bug", 1, 1, 1)

    pokemon_2 = Pokemon(0.5, 0.25, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 100, 1, 1, 1, 1, "Water Pokemon", 15, 1,
                        1, 50, "", "Eevee", 1, 1, 1, 10, 60, "water", "",
                        1, 1, 1)

    game = Game([pokemon_1, pokemon_2])
    game.set_game_mode("1")
    game.set_players()
    players = game.players()
    assert isinstance(players[0], Human) is True
    assert isinstance(players[1], Human) is True


def test_set_players_game_with_one_human():
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        10, 1, 1, 1, 1, "Fox Pokemon", 70, 1, 1, 40, "",
                        "Delphox", 1, 1, 20, 50, 30, "dark", "bug", 1, 1, 1)

    pokemon_2 = Pokemon(0.5, 0.25, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 100, 1, 1, 1, 1, "Water Pokemon", 15, 1,
                        1, 50, "", "Eevee", 1, 1, 1, 10, 60, "water", "",
                        1, 1, 1)

    game = Game([pokemon_1, pokemon_2])
    game.set_game_mode("2")
    game.set_players()
    players = game.players()
    assert isinstance(players[0], Human) is True
    assert isinstance(players[1], Computer) is True


def test_set_players_names(monkeypatch):
    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        10, 1, 1, 1, 1, "Fox Pokemon", 70, 1, 1, 40, "",
                        "Delphox", 1, 1, 20, 50, 30, "dark", "bug", 1, 1, 1)

    pokemon_2 = Pokemon(0.5, 0.25, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 100, 1, 1, 1, 1, "Water Pokemon", 15, 1,
                        1, 50, "", "Eevee", 1, 1, 1, 10, 60, "water", "",
                        1, 1, 1)

    game = Game([pokemon_1, pokemon_2])
    game.set_game_mode("1")
    game.set_players()

    player_1 = game.players()[0]
    player_2 = game.players()[1]

    game.set_players_names(["Ash", "James"])
    assert player_1.name() == "Ash"
    assert player_2.name() == "James"
