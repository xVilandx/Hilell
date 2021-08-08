import random


class _Unit:
    def __init__(self, name_unit='None', name_clan='None'):
        self.name = name_unit
        self.clan = name_clan
        self.hp = 100
        self.power = 1
        self.agility = 1
        self.intelligence = 1

    def heal(self, ):
        if self.hp > 90:
            self.hp = 100
        else:
            self.hp += 10

    def up_skill(self):
        if isinstance(self, MageUnit) and self.intelligence < 10:
            self.intelligence += 1
        elif isinstance(self, ArcherUnit) and self.agility < 10:
            self.agility += 1
        elif isinstance(self, KnightUnit) and self.power < 10:
            self.power += 1


class MageUnit(_Unit):
    def __init__(self, name_unit='None', name_clan='None'):
        super().__init__(name_unit, name_clan)
        magic = ['air', 'fire', 'water']
        self.type_magic = random.choice(magic)


class ArcherUnit(_Unit):
    def __init__(self, name_unit='None', name_clan='None'):
        super().__init__(name_unit, name_clan)
        bows = ['bow', 'crossbow']
        self.type_bow = random.choice(bows)


class KnightUnit(_Unit):
    def __init__(self, name_unit='None', name_clan='None'):
        super().__init__(name_unit, name_clan)
        weapons = ['sword', 'axe', 'peak']
        self.type_weapon = random.choice(weapons)
