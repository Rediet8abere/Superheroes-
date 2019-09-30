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
            total_damage+=ability.attack()
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
                #sets random defender based on random attacker
                if random_attacker == self:
                    random_defender = opponent
                else:
                    random_defender = self
                fight = random_attacker.take_damage(random_defender.attack())
                print(self.is_alive(), opponent.is_alive())
                # checks if either one of them are alive and sets them as a winner
                if self.is_alive() == True and opponent.is_alive() == False:
                    # print(self.name, "won!")
                    self.add_kill(1)
                    opponent.add_deaths(1)
                    # print(self.name,"kills", self.kills)
                    # print(opponent.name, "dies", opponent.deaths)
                elif opponent.is_alive() == True and self.is_alive() == False:
                    # print(opponent.name, "won!")
                    opponent.add_kill(1)
                    self.add_deaths(1)
                    # print(opponent.name,"kills", opponent.kills)
                    # print(self.name, "dies", self.deaths)
            else:
                print("Draw")
                break

    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
        self.kills = self.kills + num_kills

    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths = self.deaths + num_deaths

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
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # create another function and check if there is alive hero and return the list
        #  in the while loop check if the length of hero list is greater than one
        # print(self)
        # print(other_team)
        # print(self.heroes)
        # print(other_team.heroes)

        self_alive_hero = self.alive_hero(self.heroes)
        print("list of self alive heroes", self_alive_hero)

        other_alive_hero = self.alive_hero(other_team.heroes)
        print("list of other alive hero", other_alive_hero)


        while len(self_alive_hero) > 0 and len(other_alive_hero) > 0:

            random_selfhero = random.choice(self_alive_hero)
            print("randomely chosen self hero", random_selfhero)

            random_otherhero = random.choice(other_alive_hero)
            print("randomely chosen other hero", random_otherhero)

            random_selfhero.fight(random_otherhero)

            self_alive_hero = self.alive_hero(self.heroes)
            print("list of self alive heroes", self_alive_hero)

            other_alive_hero = self.alive_hero(other_team.heroes)
            print("list of other alive hero", other_alive_hero)



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
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        # print(self.heroes)
        # def alive_hero(self, heroes):
        #
        #     alive = []
        #
        #     for hero in heroes:
        #         if hero.is_alive():
        #             alive.append(hero)
        #     return alive

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
            # print(hero.name, "kills", hero, hero.kills)
            # print(hero.name, "dies", hero, hero.deaths)
            #     Declare winning team
            #     Show both teams average kill/death ratio.
            #     Show surviving heroes.
            kills = hero.kills+1
            deaths = hero.deaths+1
            print(hero.name, "points", (kills // deaths))
            print("alive/dead", hero.name, hero.is_alive())
            if hero.is_alive() == True:
                print("Alive Hero", hero.name)
                # print("Wining Team", self.name)
                print()

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = None
        self.team_two = None
        # TODO: create instance variables named team_one and team_two that
        # will hold our teams.

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        # TODO: This method will allow a user to create an ability.
        # Prompt the user for the necessary information to create a new ability object.
        # return the new ability object.
        ability_name = input("Please name your ability: ")
        attack_strength = input("Please enter attack strength: ")
        ability = Ability(ability_name, attack_strength)
        # print("ability in create ability", ability)
        return ability

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # TODO: This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.
        weapon_name = input("Please name your weapon: ")
        weapon_strength = input("Please enter weapon strength: ")
        weapon = Weapon(weapon_name, weapon_strength)
        # print("weapon in create weapon", weapon)
        return weapon

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor
        #  object.
        #
        #  return the new armor object with values set by user.
        armor_name = input("Please name your armor: ")
        armor_strength = input("Please enter maximum block: ")
        armor = Armor(armor_name, armor_strength)
        # print("armor in create armor", armor)
        return armor

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        # TODO: This method should allow a user to create a hero.
        # User should be able to specify if they want armors, weapons, and
        # abilities.
        # Call the methods you made above and use the return values to build
        # your hero.
        #
        # return the new hero object
        hero_name = input("Please enter hero name: ")
        hero_member = Hero(hero_name)
        # print("hero member in create hero", hero_member)

        abilities = input(f'Do you want to specify  {hero_name} abilities?(yes/no) ')
        if abilities.lower() == "yes":
            Ability = self.create_ability()
            hero_member.add_ability(Ability)
            # print("hero member ability", hero_member.abilities)

        armors = input(f'Do you want to specify  {hero_name} armors?(yes/no) ')
        if armors.lower() == "yes":
            Armor = self.create_armor()
            hero_member.add_armor(Armor)
            # print("hero member armor", hero_member.armors)

        weapons = input(f'Do you want to specify  {hero_name} weapons?(yes/no) ')
        if weapons.lower() == "yes":
            Weapon = self.create_weapon()
            hero_member.add_weapon(Weapon)
            # print("hero member weapon in ability", hero_member.abilities)
        # print(hero_member)
        return hero_member

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        team_one_name = input(" Please name your team: ")
        team_one = Team(team_one_name)
        num_ofheroes = input("How many heroes do you want in team_one? ")
        for num in range(int(num_ofheroes)):
            hero_member = self.create_hero()
            # print("hero member in team one created", hero_member)
            team_one.add_hero(hero_member)
        team_one.view_all_heroes()
        # print("team one heroes", team_one.heroes)
        self.team_one = team_one
        # print("team one", self.team_one)

    def build_team_two(self):
        '''Prompt the user to build team_two'''

        team_two_name = input(" Please name your team: ")
        team_two = Team("Sucide Squad")
        num_ofheroes = input("How many heroes do you want in team_two? ")
        for num in range(int(num_ofheroes)):
            hero_member = self.create_hero()
            # print("hero member in team team two created", hero_member)
            team_two.add_hero(hero_member)
        team_two.view_all_heroes()
        # print("team two heroes", team_two.heroes)
        self.team_two = team_two
        # print("team two", self.team_two)


    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        #     Show surviving heroes.
        print()
        print("team one status: ")
        self.team_one.stats()
        print()
        print("team two stats: ")
        self.team_two.stats()




if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
