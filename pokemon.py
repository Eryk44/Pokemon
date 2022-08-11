class Pokemon:
    def __init__(self,
                 against_bug,
                 against_dark,
                 against_dragon,
                 against_electric,
                 against_fairy,
                 against_fighting,
                 against_fire,
                 against_flying,
                 against_ghost,
                 against_grass,
                 against_ground,
                 against_ice,
                 against_normal,
                 against_poison,
                 against_psychic,
                 against_rock,
                 against_steel,
                 against_water,
                 attack,
                 base_egg_steps,
                 base_happiness,
                 base_total,
                 capture_rate,
                 classfication,
                 defence,
                 experience_growth,
                 height_m,
                 hp,
                 japanese_name,
                 name,
                 percentage_male,
                 pokedex_number,
                 sp_attack,
                 sp_defence,
                 speed,
                 type1,
                 type2,
                 weight_kg,
                 generation,
                 is_legendary,
                 increase_defence=0.1
                 ):

        self._against_bug = float(against_bug)
        self._against_dark = float(against_dark)
        self._against_dragon = float(against_dragon)
        self._against_electric = float(against_electric)
        self._against_fairy = float(against_fairy)
        self._against_fighting = float(against_fighting)
        self._against_fire = float(against_fire)
        self._against_flying = float(against_flying)
        self._against_ghost = float(against_ghost)
        self._against_grass = float(against_grass)
        self._against_ground = float(against_ground)
        self._against_ice = float(against_ice)
        self._against_normal = float(against_normal)
        self._against_poison = float(against_poison)
        self._against_psychic = float(against_psychic)
        self._against_rock = float(against_rock)
        self._against_steel = float(against_steel)
        self._against_water = float(against_water)
        self._attack = int(attack)
        self._base_egg_steps = float(base_egg_steps)
        self._base_happiness = float(base_happiness)
        self._base_total = float(base_total)
        self._capture_rate = float(capture_rate)
        self._classfication = classfication
        self._defence = int(defence)
        self._experience_growth = float(experience_growth)
        if height_m:
            self._height_m = float(height_m)
        else:
            self._height_m = 0
        self._hp = int(hp)
        self._japanese_name = japanese_name
        self._name = name
        if percentage_male:
            self._percentage_male = float(percentage_male)
        else:
            self._percentage_male = 0
        self._pokedex_number = float(pokedex_number)
        self._sp_attack = int(sp_attack)
        self._sp_defence = int(sp_defence)
        self._speed = int(speed)
        self._type1 = type1
        self._type2 = type2
        if weight_kg:
            self._weight_kg = float(weight_kg)
        else:
            self._weigh_kg = 0
        self._generation = float(generation)
        self._is_legendary = int(is_legendary)
        self._increase_defence = increase_defence

    def against_bug(self):
        return self._against_bug

    def against_dark(self):
        return self._against_dark

    def against_dragon(self):
        return self._against_dragon

    def against_electric(self):
        return self._against_electric

    def against_fairy(self):
        return self._against_fairy

    def against_fighting(self):
        return self._against_fighting

    def against_fire(self):
        return self._against_fire

    def against_flying(self):
        return self._against_flying

    def against_ghost(self):
        return self._against_ghost

    def against_grass(self):
        return self._against_grass

    def against_ground(self):
        return self._against_ground

    def against_ice(self):
        return self._against_ice

    def against_normal(self):
        return self._against_normal

    def against_poison(self):
        return self._against_poison

    def against_psychic(self):
        return self._against_psychic

    def against_rock(self):
        return self._against_rock

    def against_steel(self):
        return self._against_steel

    def against_water(self):
        return self._against_water

    def attack(self):
        return self._attack

    def base_egg_steps(self):
        return self._base_egg_steps

    def base_happiness(self):
        return self._base_happiness

    def base_total(self):
        return self._base_total

    def capture_rate(self):
        return self._capture_rate

    def classfication(self):
        return self._classfication

    def defence(self):
        return self._defence

    def experience_growth(self):
        return self._experience_growth

    def height_m(self):
        return self._height_m

    def hp(self):
        return self._hp

    def japanese_name(self):
        return self._japanese_name

    def name(self):
        return self._name

    def percentage_male(self):
        return self._percentage_male

    def pokedex_number(self):
        return self._pokedex_number

    def sp_attack(self):
        return self._sp_attack

    def sp_defence(self):
        return self._sp_defence

    def speed(self):
        return self._speed

    def type1(self):
        return self._type1

    def type2(self):
        return self._type2

    def weight_kg(self):
        return self._weight_kg

    def generation(self):
        return self._generation

    def is_legendary(self):
        return self._is_legendary

    def increase_defence(self):
        return self._increase_defence

    def take_damage(self, damage):
        self._hp -= damage

    def set_defence(self):
        self._defence = round(1.1 * self._defence)

    def __str__(self):
        return self.name()

    def basic_stats(self):
        stats = [self.hp(),
                 self.attack(),
                 self.sp_attack(),
                 self.defence(),
                 self.sp_defence()]
        return stats
