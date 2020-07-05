# 16. Imagine you are creating a Super Mario game. You need to define
# a class to represent Mario. What would it look like? If you aren't
# familiar with SuperMario, use your own favorite video or board game
# to model a player.


class Heros:
    def __init__(self):
        self.base_HP = 200
        self.base_MP = 75


class Shrapnel:
    def __init__(self):
        self.skill_name = 'Shrapnel'
        self.skilltype = ['active']
        self.affects = ['enemy']
        self.damage_type = 'magical'


class Headshot:
    def __init__(self):
        self.skill_name = 'Headshot'
        self.skilltype = ['passive']
        self.affects = ['enemy', 'allies']
        self.damage_type = 'physical'


class TakeAim:
    def __init__(self):
        self.skill_name = 'Take Aim'
        self.skilltype = ['no-target', 'passive']
        self.affects = ['enemy', 'self']


class Assasinate:
    def __init__(self):
        self.skill_name = 'Assasinate'
        self.skilltype = ['taget-unit']
        self.affects = ['enemy']
        self.damage_type = 'magical'


class Sniper(Heros, Shrapnel, Headshot, TakeAim, Assasinate):
    def __init__(self):
        self.lore_name = 'Kardel Sharpeye'
        self.base_level = 0
        self.base_movement_speed = 285
        self.bonus_movement_speed = 0
        self.base_strength = 19
        self.base_agility = 21
        self.base_intelligence = 15
        self.bonus_strength = 0
        self.bonus_agility = 0
        self.bonus_intelligence = 0
        self.effective_strength = self.base_strength + self.bonus_strength
        self.effective_agility = self.base_agility + self.bonus_agility
        self.effective_intelligence = self.base_intelligence + self.bonus_intelligence

        self.max_HP = 200 + (self.base_strength + self.bonus_strength) * 20
        self.max_MP = 75 + (self.base_intelligence +
                            self.base_intelligence) * 12
        self.base_max_damage = 25
        self.base_min_damage = 19
        self.bonus_max_damage = 0
        self.bonus_min_damage = 0
        self.effective_max_damage = self.base_max_damage + \
            self.effective_agility + self.bonus_max_damage
        self.effective_min_damage = self.base_min_damage + \
            self.effective_agility + self.bonus_min_damage

    def levelUp(self):
        self.base_level += 1
        self.base_intelligence += 2.60
        self.base_agility += 3.40
        self.base_strength += 1.70

    def set_ItemModifiers(self, items):
        if ("Divine Rapier" in items):
            self.bonus_max_damage += 330
            self.bonus_min_damage += 330


player1 = Sniper()
itemslots = ["Divine Rapier"]
player1.set_ItemModifiers(itemslots)
