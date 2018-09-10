import random


evade_message = "Has Successfully Evaded Your Attack!!"


class Characters:
    evade_message = "Has Successfully Evaded Your Attack!!"

    def __init__(self, character_class, strength, speed, hit_points, mana, character_melee_weapon,
                 character_ranged_weapon, character_magical_weapon):
        self.character_class = character_class
        self.strength = strength
        self.speed = speed
        self.hit_points = hit_points
        self.mana = mana
        self.character_melee_weapon = character_melee_weapon
        self.character_ranged_weapon = character_ranged_weapon
        self.character_magical_weapon = character_magical_weapon


class Battle(Characters):
    def melee_attacked(self):
        evade = random.randrange(1, 21)
        if evade >= self.speed:
            print("Your", User.character_melee_weapon, "Hit The", self.character_class, "!!")
            print(self.character_class, "Says: ouch! Your", User.character_melee_weapon, "Cut Me!\n")
            self.hit_points -= 10
        else:
            print("The", self.character_class, evade_message)
            print(self.character_class, ": Ha Ha Ha!!\n")

    def range_attacked(self):
        evade = random.randrange(1, 21)
        if evade >= self.speed:
            print("Your", User.character_ranged_weapon, "Hit The", self.character_class, "!!")
            print(self.character_class, "Says: Your Pebble Hurt Me Really Hard!\n")
            self.hit_points -= 15
            Battle.check_life(self)
        else:
            print("The", self.character_class, evade_message)
            print(self.character_class, ": Ha Ha Ha!!\n")

    def magic_attacked(self):
        evade = random.randrange(1, 21)
        if evade >= self.speed:
            print("You Throw A Huge Ball Of Fire At The", self.character_class, "!!")
            print("Your", User.character_magical_weapon, "Hit The", self.character_class, "!!")
            print(self.character_class, "Says: I'm Burning!!")
            self.hit_points -= 35
            Battle.check_life(self)
        else:
            print("The", self.character_class, evade_message, "\n")
            print(self.character_class, ": Ha Ha Ha!!\n")

    def check_life(self):
        if self.hit_points <= 0:
            print("The", self.character_class, "Is Dead..  You Win!!\n\n")
        else:
            print("The", self.character_class, "Now Has", self.hit_points, "Hit Points Left\n")

    def character_heal(self):
        heal_number = random.randrange(1, 26)
        if heal_number <= self.speed * 2:
            print("The Mighty", self.character_class, "Failed To Cast A Healing Spell And Suffers A", heal_number,
                  "Hit Points Penalty\n")
            self.hit_points -= heal_number
            Battle.check_life(self)
        else:
            print("The Mighty", self.character_class, "Successfully Casts A Healing Spell")
            a = random.randrange(1, self.mana + 1)
            print(a, "Hit Points Were Restored\n")
            self.hit_points += a
            Battle.check_life(self)

    def user_attacked(self):
        evade = random.randrange(1, 21)
        a = random.randrange(1, 4)
        if a == 1:
            print("The Mighty", self.character_class, "Attacks You With His", self.character_melee_weapon, "\n")
            if evade >= self.speed:
                print("You Evaded The", self.character_melee_weapon, "!!\n")
            else:
                print("You Were Hit By The", self.character_melee_weapon, "And It Hurts.. Alot..")
                User.hit_points -= self.strength * a
        elif a == 2:
            print("The Mighty", self.character_class, "Attacks You With His", self.character_ranged_weapon, "\n")
            if evade >= self.speed:
                print("You Evaded The", self.character_ranged_weapon, "!!\n")
            else:
                print("You Were Hit By The", self.character_ranged_weapon, "And It Hurts.. Alot..")
                User.hit_points -= random.randrange(self.strength * a + 1)
        elif a == 3:
            print("The Mighty", self.character_class, "Attacks You With His", self.character_magical_weapon, "\n")
            if evade >= self.speed:
                print("You Evaded The", self.character_magical_weapon, "!!\n")
            else:
                print("You Were Hit By The", self.character_ranged_weapon, "And It Hurts.. Alot..")
                User.hit_points -= random.randrange(self.strength * a)
        else:
            print("chambawamba")

    def user_check_life(self):
        if User.hit_points <= 0:
            print("The", User.character_class, "Is Slain By The..", self.character_class, "You Lose!!")
        else:
            print("You, a.k.a \"The", User.character_class, "\" Now Have",
                  User.hit_points, "Hit Points Left\n\n")

    def user_heal(self):
        heal_number = random.randrange(1, 26)
        if heal_number <= self.speed * 2:
            print("The Mighty", User.character_class, "Failed To Cast A Healing Spell And Suffers A", heal_number,
                  "Hit Points Penalty\n")
            User.hit_points -= heal_number
            Battle.user_check_life(self)
        else:
            print("The Mighty", User.character_class, ", That's You, Successfully Casted A Healing Spell")
            a = random.randrange(User.mana + 1)
            print(a, "Hit Points Were Restored\n\n")
            User.hit_points += a
            Battle.user_check_life(self)


User = Characters(character_class="Knight", strength=10, speed=5, hit_points=100, mana=40,
                  character_melee_weapon="Huge BroadSword",
                  character_ranged_weapon="Very Accurate Sling",
                  character_magical_weapon="Magical Wand")
Warrior = Characters(character_class="Warrior", strength=8, speed=6, hit_points=100, mana=10,
                     character_melee_weapon="Very Big Club",
                     character_ranged_weapon="Composite Bow",
                     character_magical_weapon="Magical Fire-Sword")
Archer = Characters(character_class="Archer", strength=6, speed=8, hit_points=80, mana=20,
                    character_melee_weapon="Tiny Sharp Dagger",
                    character_ranged_weapon="Long Bow",
                    character_magical_weapon="Exploding Magic Arrow")
Mage = Characters(character_class="Mage", strength=4, speed=4, hit_points=60, mana=50,
                  character_melee_weapon="Long Wooden Saff",
                  character_ranged_weapon="A Bright Lightning Bolt",
                  character_magical_weapon="Horrible Dark Magic")
Dragon = Characters(character_class="Dragon", strength=12, speed=10, hit_points=120, mana=30,
                    character_melee_weapon="Nasty Long Claw",
                    character_ranged_weapon="Fiery Breath",
                    character_magical_weapon="Great Business Skill")
Unicorn = Characters(character_class="Unicorn", strength=14, speed=12, hit_points=140, mana=40,
                     character_melee_weapon="Pointy Silver Horn",
                     character_ranged_weapon="Awful Disco Song",
                     character_magical_weapon="Mistaking Innocence")


def run(x):
    print("\nSo, You Have Chosen To Fight The Great", x.character_class, ", ", x.character_class, "ous!!\n")
    while x.hit_points > 0 and User.hit_points > 0:
        a = (input("Choose Your Attack!! \n 1. Melee Attack \n 2. Ranged Attack \n 3. Magic Attack \n"))
        if a == "1":
            Battle.melee_attacked(x)
            Battle.character_heal(x)
            Battle.user_attacked(x)
            Battle.user_heal(x)
        elif a == "2":
            Battle.range_attacked(x)
            Battle.character_heal(x)
            Battle.user_attacked(x)
            Battle.user_heal(x)
        elif a == "3":
            Battle.magic_attacked(x)
            Battle.character_heal(x)
            Battle.user_attacked(x)
            Battle.user_heal(x)
        else:
            print(a, "Is Not A Valid Attack Number! Try Again!! ")
    else:
        print("Game Over")


def game():
    y = int(input("\nHello Young Knight! \nWhat Beast Would You Like To Fight??\n\n "
                  "1. The Fiersome Warrior \n 2. The Master Archer \n 3. The Arch-Mage \n "
                  "4. The AllMighty Dragon \n 5. The Bewitched Unicorn \n"))
    if y == 1:
        run(Warrior)
    elif y == 2:
        run(Archer)
    elif y == 3:
        run(Mage)
    elif y == 4:
        run(Dragon)
    elif y == 5:
        run(Unicorn)
    else:
        print("Coward!!")


game()
