from random import uniform


class Pair():
    def __init__(self, player, pokemon=None):
        self._player = player
        self._pokemon = pokemon
        self._miss_turn = False

    def player(self):
        return self._player

    def pokemon(self):
        return self._pokemon

    def move(self):
        return self._move

    def current_move(self, move):
        self._move = move

    def set_enemy(self, pairs):
        enemy = [pair for pair in pairs if pair != self]
        self._enemy = enemy[0]

    def set_miss_turn(self, value):
        self._miss_turn = value

    def miss_turn(self):
        return self._miss_turn

    def enemy(self):
        return self._enemy

    def speed(self):
        return self.pokemon().speed()

    def make_move(self):
        decision = self.move()

        if decision == "1":
            self.defence()

        elif decision == "2":
            self.attack()

        elif decision == "3":
            self.special_attack()

        elif decision == "4":
            self.change_pokemon()

    def __eq__(self, other_pair):
        return self.player().name() == other_pair.player().name()

    def change_pokemon(self, new_pokemon):
        self._pokemon = new_pokemon

    def defence(self):
        pokemon = self.pokemon()
        pokemon.set_defence()

    def attack(self):
        pokemon = self.pokemon()
        enemy = self.enemy()
        enemy_pokemon = self.enemy().pokemon()
        modifier = enemy_pokemon.against_normal() * uniform(0.85, 1)
        damage = round((3 * (pokemon.attack() / enemy_pokemon.defence()) + 2)
                       * modifier)
        self.attack_enemy_pokemon(damage, enemy_pokemon, enemy)
        return damage

    def special_attack(self, chosen_type):
        pokemon = self.pokemon()
        enemy = self.enemy()
        enemy_pokemon = self.enemy().pokemon()

        type_resistance = getattr(enemy_pokemon, f"against_{chosen_type}")()
        modifier = type_resistance * uniform(0.85, 1)
        damage = round((3 * (pokemon.sp_attack() / enemy_pokemon.sp_defence())
                        + 2) * modifier)
        self.attack_enemy_pokemon(damage, enemy_pokemon, enemy)
        return damage

    def attack_enemy_pokemon(self, damage, enemy_pokemon, enemy):
        enemy_pokemon.take_damage(damage)
        if enemy_pokemon.hp() <= 0:
            enemy.player().remove_pokemon(enemy_pokemon)
            enemy.set_miss_turn(True)
