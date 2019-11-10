from random import randrange


class MSDie:

    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides+1)

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


die1 = MSDie(6)
print(die1.value)
die1.roll()
print(die1.value)
