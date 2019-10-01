import random

class Ability:

    def __init__(self, name, attack_strength):
        '''Create Instance Variables:
          name:String
          max_damage: Integer
       '''
        self.name = name
        self.max_damage = int(attack_strength)

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
        self.max_block = int(max_block)
    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''
        return random.randint(0, self.max_block)

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
        self.starting_health = int(starting_health)
        self.current_health = int(starting_health)
        self.abilities = []
        self.armors = []
        self.deaths = 0
        self.kills = 0

    def add_ability(self, Ability):
        ''' Add ability to abilities list '''
        self.abilities.append(Ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
        return: total:Int
        '''
        total_damage = 0
        for ability in self.abilities:
            total_damage+=int(ability.attack())
        return total_damage

    def add_armor(self, Armor):
        '''Add armor to self.armors
        Armor: Armor Object
        '''
        self.armors.append(Armor)

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
        take_damage = self.defend(int(damage))
        self.current_health -= take_damage

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.'''
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.'''
        while self.current_health > 0 and opponent.current_health > 0:
            if self.attack() > 0 or opponent.attack() > 0:
                # generates a random attacker to be fair
                random_attacker = random.choice([self, opponent])
                if random_attacker == self:
                    random_defender = opponent
                else:
                    random_defender = self
                fight = random_attacker.take_damage(random_defender.attack())
                print(self.is_alive(), opponent.is_alive())
                if self.is_alive() == True and opponent.is_alive() == False:
                    self.add_kill(1)
                    opponent.add_deaths(1)
                    print(self.name, "kill amt", self.kills)
                    print(opponent.name, "death amt", opponent.deaths)
                elif opponent.is_alive() == True and self.is_alive() == False:
                    # print(opponent.name, "won!")
                    opponent.add_kill(1)
                    self.add_deaths(1)
                    print(opponent.name, "kill amt", opponent.kills)
                    print(self.name, "death amt", self.deaths)
            else:
                print("Draw")
                self.current_health = 0
                opponent.current_health = 0


    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
        self.kills = self.kills + num_kills

    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths = self.deaths + num_deaths

    def results(self, opponent):
        pass

    def add_weapon(self, Weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(Weapon)


class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """

        return random.randint(self.max_damage//2, self.max_damage)

class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name'''
        self.name = name
        self.heroes = [] # contain objects of type (HERO)

    def remove_hero(self, name):
        '''Remove hero from heroes list. If Hero isn't found return 0. '''
        for hero in self.heroes:
            self.heroes.remove(hero)
        return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        print(self.name, ":")
        # print(self.heroes)
        for hero in self.heroes:
            print(hero.name, hero)
            print()

    def add_hero(self, Hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(Hero)

    def alive_hero(self, heroes):

        alive = []
        for hero in heroes:
            if hero.is_alive():
                alive.append(hero)
        return alive

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        self_alive_hero = self.alive_hero(self.heroes)
        other_alive_hero = self.alive_hero(other_team.heroes)
        while len(self_alive_hero) > 0 and len(other_alive_hero) > 0:
            random_selfhero = random.choice(self_alive_hero)
            random_otherhero = random.choice(other_alive_hero)
            random_selfhero.fight(random_otherhero)
            self_alive_hero = self.alive_hero(self.heroes)
            other_alive_hero = self.alive_hero(other_team.heroes)


    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            print(hero.current_health)
            hero.current_health = health
            print(hero.current_health)

    def stats(self):
        '''Print team statistics'''
        living_heroes = self.alive_hero(self.heroes)
        if len(living_heroes) > 0:
            print("Wining Team", self.name)
            print()
        else:
            print("Losing Team", self.name)
            print()

        kills = 0
        deaths = 0
        for hero in self.heroes:
            kills = hero.kills+1
            deaths = hero.deaths+1
            print(hero.name, "points: ")
            print(int((kills / deaths)*100))
            print(hero.name, "kill amt", hero.kills)
            print(hero.name, "death amt", hero.deaths)
            print("alive/dead", hero.name, hero.is_alive())
            if hero.is_alive() == True:
                print("Alive Hero", hero.name)
                print()

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = None
        self.team_two = None
    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        ability_name = input("Please name your ability: ")
        attack_strength = input("Please enter attack strength: ")
        ability = Ability(ability_name, attack_strength)
        return ability

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        weapon_name = input("Please name your weapon: ")
        weapon_strength = input("Please enter weapon strength: ")
        weapon = Weapon(weapon_name, weapon_strength)
        return weapon

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        armor_name = input("Please name your armor: ")
        armor_strength = input("Please enter maximum block: ")
        armor = Armor(armor_name, armor_strength)
        return armor

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Please enter hero name: ")
        hero_member = Hero(hero_name)

        abilities = input(f'Do you want to specify  {hero_name} abilities?(yes/no) ')
        if abilities.lower() == "yes":
            Ability = self.create_ability()
            hero_member.add_ability(Ability)

        armors = input(f'Do you want to specify  {hero_name} armors?(yes/no) ')
        if armors.lower() == "yes":
            Armor = self.create_armor()
            hero_member.add_armor(Armor)

        weapons = input(f'Do you want to specify  {hero_name} weapons?(yes/no) ')
        if weapons.lower() == "yes":
            Weapon = self.create_weapon()
            hero_member.add_weapon(Weapon)
        return hero_member

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        team_one_name = input(" Please name your team one: ")
        team_one = Team(team_one_name)
        num_ofheroes = input("How many heroes do you want in team_one? ")
        for num in range(int(num_ofheroes)):
            hero_member = self.create_hero()
            team_one.add_hero(hero_member)
        team_one.view_all_heroes()
        self.team_one = team_one

    def build_team_two(self):
        '''Prompt the user to build team_two'''

        team_two_name = input(" Please name your team two: ")
        team_two = Team(team_two_name)
        num_ofheroes = input("How many heroes do you want in team_two? ")
        for num in range(int(num_ofheroes)):
            hero_member = self.create_hero()
            team_two.add_hero(hero_member)
        team_two.view_all_heroes()
        self.team_two = team_two

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        print()
        print("team one status: ")
        self.team_one.stats()
        print()
        print("team two stats: ")
        self.team_two.stats()

    def edit(self, team):
        print(team)
        for hero in team.heroes:
            print("team member", hero)
            change = input(f"what changes would you like to make to {hero.name} ability(ab)and weapon/armor(ar)? ")
            if change.lower() == "ab":
                print(hero.abilities)
                for ability in hero.abilities:
                    print("Before change", ability.name)
                    ability_name = input(f"Update ability name {ability.name}: ")
                    ability.name = ability_name
                    print("After change", ability.name)
                    print()
                    print("Before change", ability.max_damage)
                    max_damage = input(f"Update max damage {ability.max_damage}: ")
                    ability.max_damage = max_damage
                    print("After change", ability.max_damage)

            elif change.lower() == "ar":
                print(hero.armors)
                for armor in hero.armors:
                    print(armor.name)
                    armor_name = input(f"Update ability name {armor.name}: ")
                    armor.name = armor_name
                    print("After change", armor.name)
                    print()
                    print("Before change", armor.max_block)
                    max_block = input(f"Update max damage {armor.max_block}: ")
                    armor.max_block = max_block
                    print("After change", armor.max_block)
            elif change.lower() == "we":
                pass
            self.team_battle()


    def recreate_or_edit(self):
        '''Add a command line interface that allows for recreating or editing of teams. '''
        recreate_or_edit = input("Do you want to recreate or edit your teams? r or e: ")
        if recreate_or_edit.lower() == "r":
            self.build_team_one()
            self.build_team_two()
        else:
            team = input("which team do you want to edit? (Please put the same spelling)")
            if team == self.team_one.name:
                print("team one object in re", self.team_one)
                self.edit(self.team_one)
            else:
                print("team two object in re", self.team_two)
                self.edit(self.team_two)
        self.team_battle()


if __name__ == "__main__":
    game_is_running = True
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")
        if play_again.lower() == "n":
            game_is_running = False
        else:
            revive_or_updates = input("Play with the revive or update heroes(u/r) : ")
            if recreate_or_updates.lower() == "u":
                arena.recreate_or_edit()
            else:
                arena.team_one.revive_heroes()
                arena.team_two.revive_heroes()
