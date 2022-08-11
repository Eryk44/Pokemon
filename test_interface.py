from interface import Interface
from pokemon import Pokemon


def test_read_from_pokemons():
    interface = Interface()

    with open("test_pokemon.csv", mode='r') as handle:
        pokemons = interface.read_from_pokemons(handle)

    assert pokemons[0].against_bug() == 1
    assert pokemons[0].against_dark() == 2
    assert pokemons[0].against_dragon() == 3
    assert pokemons[0].against_electric() == 4
    assert pokemons[0].against_fairy() == 5
    assert pokemons[0].against_fighting() == 6
    assert pokemons[0].against_fire() == 7
    assert pokemons[0].against_flying() == 8
    assert pokemons[0].against_ghost() == 9
    assert pokemons[0].against_grass() == 10
    assert pokemons[0].against_ground() == 11
    assert pokemons[0].against_ice() == 12
    assert pokemons[0].against_normal() == 13
    assert pokemons[0].against_poison() == 14
    assert pokemons[0].against_psychic() == 15
    assert pokemons[0].against_rock() == 16
    assert pokemons[0].against_steel() == 17
    assert pokemons[0].against_water() == 18
    assert pokemons[0].attack() == 19
    assert pokemons[0].base_egg_steps() == 20
    assert pokemons[0].base_happiness() == 21
    assert pokemons[0].base_total() == 22
    assert pokemons[0].capture_rate() == 23
    assert pokemons[0].classfication() == "Electric Pokemon"
    assert pokemons[0].defence() == 24
    assert pokemons[0].experience_growth() == 25
    assert pokemons[0].height_m() == 26
    assert pokemons[0].hp() == 27
    assert pokemons[0].japanese_name() == ""
    assert pokemons[0].name() == "Pikachu"
    assert pokemons[0].percentage_male() == 28
    assert pokemons[0].pokedex_number() == 29
    assert pokemons[0].sp_attack() == 30
    assert pokemons[0].sp_defence() == 31
    assert pokemons[0].speed() == 32
    assert pokemons[0].type1() == "electric"
    assert pokemons[0].type2() == ""
    assert pokemons[0].weight_kg() == 33
    assert pokemons[0].generation() == 34
    assert pokemons[0].is_legendary() == 0


def test_get_pokemon_by_name():
    interface = Interface()

    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        10, 1, 1, 1, 1, "Fox Pokemon", 70, 1, 1, 40, "",
                        "Delphox", 1, 1, 20, 50, 30, "dark", "bug", 1, 1, 1)

    pokemon_2 = Pokemon(0.5, 0.25, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 100, 1, 1, 1, 1, "Water Pokemon", 15, 1,
                        1, 50, "", "Eevee", 1, 1, 1, 10, 60, "water", "",
                        1, 1, 1)

    pokemon_3 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, "Electric Pokemon", 1, 1, 1, 1, "",
                        "Pikachu", 1, 1, 1, 1, 1, "electricity", "", 1, 1, 1)

    pokemon = interface.get_pokemon_by_name(
                                            [pokemon_1, pokemon_2, pokemon_3],
                                            "Pikachu")

    assert pokemon == pokemon_3


def test_get_pokemon_by_name_pokemon_not_in_pokemons():
    interface = Interface()

    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        10, 1, 1, 1, 1, "Fox Pokemon", 70, 1, 1, 40, "",
                        "Delphox", 1, 1, 20, 50, 30, "dark", "bug", 1, 1, 1)

    pokemon_2 = Pokemon(0.5, 0.25, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 100, 1, 1, 1, 1, "Water Pokemon", 15, 1,
                        1, 50, "", "Eevee", 1, 1, 1, 10, 60, "water", "",
                        1, 1, 1)

    pokemon_3 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, "Electric Pokemon", 1, 1, 1, 1, "",
                        "Pikachu", 1, 1, 1, 1, 1, "electricity", "", 1, 1, 1)

    pokemon = interface.get_pokemon_by_name(
                                            [pokemon_1, pokemon_2, pokemon_3],
                                            "Bulbazaur")

    assert pokemon is None


def test_create_list_of_rows():
    interface = Interface()

    pokemon_1 = Pokemon(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        10, 1, 1, 1, 1, "Fox Pokemon", 70, 1, 1, 40, "",
                        "Delphox", 1, 1, 20, 50, 30, "dark", "bug", 1, 1, 1)

    pokemon_2 = Pokemon(0.5, 0.25, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 100, 1, 1, 1, 1, "Water Pokemon", 15, 1,
                        1, 50, "", "Eevee", 1, 1, 1, 10, 60, "water", "",
                        1, 1, 1)

    rows = interface.create_list_of_rows([pokemon_1, pokemon_2])

    assert rows == [["Delphox", 40, 30, 10, 20, 70, 50],
                    ["Eevee", 50, 60, 100, 1, 15, 10]]


def test_chceck_if_not_correct_name_mode_1_correct():
    interface = Interface()

    name = "Ash"
    names = ["James"]

    assert interface.chceck_if_not_correct_name(name, names, "1") is False


def test_chceck_if_not_correct_name_mode_1_not_correct_repetition():
    interface = Interface()

    name = "Ash"
    names = ["Ash"]

    assert interface.chceck_if_not_correct_name(name, names, "1") is True


def test_chceck_if_not_correct_name_mode_1_not_correct_empty_name():
    interface = Interface()

    name = ""
    names = ["James"]

    assert interface.chceck_if_not_correct_name(name, names, "1") is True


def test_chceck_if_not_correct_name_mode_2_correct():
    interface = Interface()

    name = "Ash"
    names = []

    assert interface.chceck_if_not_correct_name(name, names, "2") is False


def test_chceck_if_not_correct_name_mode_2_not_correct():
    interface = Interface()

    name = "Computer"
    names = []

    assert interface.chceck_if_not_correct_name(name, names, "2") is True


def test_choose_game_mode(monkeypatch):
    interface = Interface()

    def give_one(a):
        return "1"

    monkeypatch.setattr("builtins.input", give_one)

    decision = interface.choose_game_mode()
    assert decision == "1"
