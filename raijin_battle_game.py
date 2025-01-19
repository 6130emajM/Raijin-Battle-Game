import random

# Base Character Class
class Character:
    def __init__(self, name, health, attack_power, max_health):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = max_health

    def attack(self):
        damage = random.randint(self.attack_power - 3, self.attack_power + 3)
        return damage

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        return f"{self.name} healed for {amount} health points. Current health: {self.health}."


# Raijin Class
class Raijin(Character):
    def __init__(self):
        super().__init__(name="Raijin", health=110, attack_power=14, max_health=110)

    def thunder_strike(self):
        # High-damage single attack
        damage = random.randint(20, 30)
        return damage

    def storm_shield(self):
        # Temporary defense boost
        return "Storm Shield activated! Raijin will take 50% less damage on the next attack."


# Evil Wizard Class
class EvilWizard(Character):
    def __init__(self):
        super().__init__("Evil Wizard", health=150, attack_power=10, max_health=150)

    def regenerate(self):
        regen = random.randint(5, 15)
        self.health += regen
        if self.health > self.max_health:
            self.health = self.max_health
        return f"Evil Wizard regenerated {regen} health points. Current health: {self.health}."


# Battle System
def battle(hero, wizard):
    print("\n⚔️ Let the battle begin! ⚔️")
    shield_active = False

    while hero.health > 0 and wizard.health > 0:
        print("\nChoose your action:")
        print("1. Attack")
        print("2. Use Thunder Strike (Special Ability)")
        print("3. Use Storm Shield (Special Ability)")
        print("4. Heal")
        print("5. View Stats")
        action = input("> ")

        if action == "1":
            damage = hero.attack()
            wizard.health -= damage
            print(f"{hero.name} attacks and deals {damage} damage!")
        elif action == "2":
            damage = hero.thunder_strike()
            wizard.health -= damage
            print(f"{hero.name} uses Thunder Strike and deals {damage} damage!")
        elif action == "3":
            shield_active = True
            print(hero.storm_shield())
        elif action == "4":
            heal_amount = random.randint(10, 20)
            print(hero.heal(heal_amount))
        elif action == "5":
            print(f"{hero.name} - Health: {hero.health}/{hero.max_health}")
            print(f"Evil Wizard - Health: {wizard.health}/{wizard.max_health}")
        else:
            print("Invalid action. Choose again.")

        # Wizard's Turn
        if wizard.health > 0:
            damage = wizard.attack()
            if shield_active:
                damage //= 2
                shield_active = False
            hero.health -= damage
            print(f"The Evil Wizard attacks and deals {damage} damage!")

            # Wizard regenerates health after its turn
            regen_message = wizard.regenerate()
            print(regen_message)

        # Display health status
        print(f"\n{hero.name} - Health: {hero.health}/{hero.max_health}")
        print(f"Evil Wizard - Health: {wizard.health}/{wizard.max_health}")

    # End of Battle
    if hero.health <= 0:
        print("\n💀 You have been defeated by the Evil Wizard. Game Over!")
    elif wizard.health <= 0:
        print("\n🎉 Congratulations! Raijin has defeated the Evil Wizard!")


# Main Menu
def main():
    print("Welcome to the Hero vs. Evil Wizard Battle Game!")
    print("Your hero is Raijin, the Thunder God of Japanese Mythology!")
    
    hero = Raijin()
    wizard = EvilWizard()
    battle(hero, wizard)


if __name__ == "__main__":
    main()
