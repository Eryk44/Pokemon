import random


class BattleGround:
    def __init__(self, pairs):
        self._pairs = pairs

    def pairs(self):
        return self._pairs

    def speed_comparison(self):
        pair_1 = self.pairs()[0]
        pair_2 = self.pairs()[1]
        pairs = [pair_1, pair_2]

        speed_1 = pair_1.speed()
        speed_2 = pair_2.speed()

        if speed_1 == speed_2:
            random.shuffle(pairs)
            return pairs

        elif speed_1 > speed_2:
            return [pair_1, pair_2]

        else:
            return [pair_2, pair_1]

    def winner(self):
        for pair in self.pairs():
            if len(pair.player().pokemons()) != 0:
                return pair.player()
            else:
                pass
