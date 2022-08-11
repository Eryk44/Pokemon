from pokemon import Pokemon


def test_create_pokemon():
    pokemon = Pokemon(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,\
         23, "Electric Pokemon", 24, 25, 26, 27, "", "Pikachu", 28, 29, 30, 31, 32, "electric", "", 33, 34, 0)

    assert pokemon.against_bug() == 1
    assert pokemon.against_dark() == 2
    assert pokemon.against_dragon() == 3
    assert pokemon.against_electric() == 4
    assert pokemon.against_fairy() == 5
    assert pokemon.against_fighting() == 6
    assert pokemon.against_fire() == 7
    assert pokemon.against_flying() == 8
    assert pokemon.against_ghost() == 9
    assert pokemon.against_grass() == 10
    assert pokemon.against_ground() == 11
    assert pokemon.against_ice() == 12
    assert pokemon.against_normal() == 13
    assert pokemon.against_poison() == 14
    assert pokemon.against_psychic() == 15
    assert pokemon.against_rock() == 16
    assert pokemon.against_steel() == 17
    assert pokemon.against_water() == 18
    assert pokemon.attack() == 19
    assert pokemon.base_egg_steps() == 20
    assert pokemon.base_happiness() == 21
    assert pokemon.base_total() == 22
    assert pokemon.capture_rate() == 23
    assert pokemon.classfication() == "Electric Pokemon"
    assert pokemon.defence() == 24
    assert pokemon.experience_growth() == 25
    assert pokemon.height_m() == 26
    assert pokemon.hp() == 27
    assert pokemon.japanese_name() == ""
    assert pokemon.name() == "Pikachu"
    assert pokemon.percentage_male() == 28
    assert pokemon.pokedex_number() == 29
    assert pokemon.sp_attack() == 30
    assert pokemon.sp_defence() == 31
    assert pokemon.speed() == 32
    assert pokemon.type1() == "electric"
    assert pokemon.type2() == ""
    assert pokemon.weight_kg() == 33
    assert pokemon.generation() == 34
    assert pokemon.is_legendary() == 0

def test_take_damage():
    pokemon = Pokemon(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,\
         23, "Electric Pokemon", 24, 25, 26, 27, "", "Pikachu", 28, 29, 30, 31, 32, "electric", "", 33, 34, 0)

    pokemon.take_damage(7)

    assert pokemon.hp() == 20


def test_set_defence():
    pokemon = Pokemon(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,\
         23, "Electric Pokemon", 30, 25, 26, 27, "", "Pikachu", 28, 29, 30, 31, 32, "electric", "", 33, 34, 0)


    pokemon.set_defence()

    assert pokemon.defence() == 33


def test_basic_stats():
    pokemon = Pokemon(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,\
         23, "Electric Pokemon", 24, 25, 26, 27, "", "Pikachu", 28, 29, 30, 31, 32, "electric", "", 33, 34, 0)

    assert pokemon.basic_stats() == [27, 19, 30, 24, 31]

