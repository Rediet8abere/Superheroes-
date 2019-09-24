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
        self.deaths = 0
        self.kills = 0

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
                if self.is_alive() and opponent.is_alive() == False:
                    print(self.name, "won!")
                    self.add_kill(1)
                    opponent.add_deaths(1)
                    print(self.name,"kills", self.kills)
                    print(opponent.name, "dies", opponent.deaths)
                elif opponent.is_alive() and self.is_alive() == False:
                    print(opponent.name, "won!")
                    self.add_deaths(1)
                    opponent.add_deaths(1)
                    print(self.name,"kills", self.kills)
                    print(opponent.name, "dies", opponent.deaths)
            else:
                print("Draw")
                break

        #... The code you already wrote should be here ...

        #TODO: Refactor this method to update the
        # number of kills the hero has when the opponent dies.
        # Also update the number of deaths for whoever dies in the fight
        pass
    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
        # TODO: This method should add the number of kills to self.kills
        self.kills = self.kills + num_kills
    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
        # TODO: This method should add the number of deaths to self.deaths
        self.deaths = self.deaths + num_deaths


class Weapon(Ability):
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
        for hero in self.heroes:
            self.heroes.remove(hero)
        return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        print(self.heroes)
        print(other_team.heroes)
        random_selfhero = random.choice(self.heroes)
        print(random_selfhero)
        random_otherhero = random.choice(other_team.heroes)
        print(random_otherhero)
        Hero.fight(random_selfhero, random_otherhero)
        # Hint: Use the fight method in the Hero class.


    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
        Hero.starting_health = health

    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        for hero in self.heroes:
            print(Hero.kills // Hero.deaths)


if __name__ == "__main__":
    team_one = Team("One")
    jodie = Hero("Jodie Foster")
    aliens = Ability("Alien Friends", 10000)
    jodie.add_ability(aliens)
    team_one.add_hero(jodie)

    team_two = Team("Two")
    athena = Hero("Athena")
    socks = Armor("Socks", 10)
    athena.add_armor(socks)
    team_two.add_hero(athena)

    assert team_two.heroes[0].deaths == 0
    team_one.attack(team_two)
    assert team_two.heroes[0].deaths == 1
