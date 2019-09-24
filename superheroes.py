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

        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

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

    def defend(self, damage_amt=0):
      '''Runs `block` method on each armor.
          Returns sum of all blocks
      '''
      total_defend = 0
      for armor in self.armors:
          block = int(armor.block())
          total_defend += block
      return abs(total_defend - damage_amt)


    def take_damage(self, damage):

        '''Updates self.current_health to reflect the damage minus the defense.'''
        # damage = damage - self.defend(damage)
        # self.current_health -= damage
        take_damage = self.defend(damage)
        self.current_health -= take_damage

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.'''
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.'''
        # TODO: Fight each hero until a victor emerges.
        # Print the victor's name to the screen.
        print(self.attack())
        print(opponent.attack())
        print("self object ", self)
        print("opponent object ", opponent)
        while self.current_health > 0 and opponent.current_health > 0:
            if self.attack() > 0 or opponent.attack() > 0:
                # generates a random attacker to be fair
                random_attacker = random.choice([self, opponent])
                print("random_attacker ", random_attacker)
                #sets random defender based on random attacker
                if random_attacker == self:
                    random_defender = opponent
                    print("random_defender ", random_defender)
                else:
                    random_defender = self
                    print("random_defender ", random_defender)
                fight = random_attacker.take_damage(random_defender.attack())
                print(self.is_alive(), opponent.is_alive())
                # checks if either one of them are alive and sets them as a winner
                if self.is_alive():
                    print(self.name, "won!")
                else:
                    print(opponent.name, "won!")
            else:
                print("Draw")
                break


class Weapon(Ability):
    # def __init__(self, name, attack_strength):
    #     # Initialize person object with name
    #     super().__init__(name, attack_strength)

    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """

        return random.randint(self.max_damage//2, self.max_damage)

class Team():
    def __init__(self, name):
        ''' Initialize your team with its team name'''
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        '''Remove hero from heroes list. If Hero isn't found return 0. '''
        # TODO: Implement this method to remove the hero from the list given their name.
        for hero in self.heroes:
            self.heroes.remove(hero)
        return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # TODO: Loop over the list of heroes and print their names to the terminal.
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)

if __name__ == "__main__":
    # team1 = Team("Awesome")
    # team1.remove_hero("spiderman")
    # print(team1.heroes)
    # team1.view_all_heroes()
    # team1.add_hero("wonderwoman")
    # team1.add_hero("batman")
    # team1.view_all_heroes()
    # team1.remove_hero("wonderwoman")
    # team1.view_all_heroes()
    # team = Team("One")
    # jodie = Hero("Jodie Foster")
    # team.add_hero(jodie)
    # # assert team.heroes[0].name == "Jodie Foster"
    # print(team.heroes[0].name)
    # team.view_all_heroes()
    # team.remove_hero("Jodie Foster")
    # team.view_all_heroes()
    # print(len(team.heroes))
    team = Team("One")
    jodie = Hero("Jodie Foster")
    team.add_hero(jodie)

    athena = Hero("Athena")
    team.add_hero(athena)
    team.view_all_heroes()
    # output_string = capture_console_output(team.view_all_heroes)

#     hero1 = Hero("Wonder Woman")
#     hero2 = Hero("Dumbledore")
#     ability1 = Ability("Super Speed", 300)
#     ability2 = Ability("Super Eyes", 130)
#     ability3 = Ability("Wizard Wand", 80)
#     ability4 = Ability("Wizard Beard", 20)
#     hero1.add_ability(ability1)
#     hero1.add_ability(ability2)
#     hero2.add_ability(ability3)
#     hero2.add_ability(ability4)
#     hero1.fight(hero2)
