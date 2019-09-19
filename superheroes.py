import random

class Ability:

    def __init__(self, name, attack_strength):
        ''' Initalizes instance variable '''
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        return random.randint(0, self.max_damage)



if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
