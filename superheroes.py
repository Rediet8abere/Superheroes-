import random

class Ability:

    def __init__(self, name, attack_strength):
        '''Create Instance Variables:
          name:String
          max_damage: Integer
       '''
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        return random.randint(0, self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block
    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''
        return random.randint(0, self.max_block )

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
          '''
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def attack(self):
      '''Calculate the total damage from all ability attacks.
          return: total:Int
      '''
      total_damage = 0
      for ability in self.abilities:
          total_damage+=ability.attack()
      return total_damage

    def add_armor(self, armor):
      '''Add armor to self.armors
        Armor: Armor Object
      '''
      self.armors.append(armor)

    def defend(self, damage_amt):
      '''Runs `block` method on each armor.
          Returns sum of all blocks
      '''

      total_defend = 0
      for armor in self.armors:
          total_defend += armor.block()
      return total_defend


    def take_damage(self, damage):

        '''Updates self.current_health to reflect the damage minus the defense.'''
        damage = damage - self.defend(damage)
        self.current_health -= damage
        # self.current_health -= self.defend(damage)
        # return self.current_health

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.'''
        if self.current_health <= 0:
            return False
        else:
            return True
        # return self.current_health



if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
