import time
import random

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        # 0 = Starving, 100 = Full
        self.hunger = 50  
        # 0 = Depressed, 100 = Euphoric
        self.happiness = 50 
        self.is_alive = True

    def feed(self):
        """Reduces hunger and slightly improves mood."""
        if not self.is_alive:
            print(f"👻 {self.name} is a ghost. You can't feed ghosts.")
            return

        print(f"\n🍖 You give {self.name} a treat...")
        time.sleep(1)
        
        self.hunger += 20
        self.happiness += 5
        
        if self.hunger > 100: self.hunger = 100
        if self.happiness > 100: self.happiness = 100
        
        print(f"😋 {self.name} loved it! Hunger is now {self.hunger}/100.")

    def play(self):
        """Increases happiness but makes the pet hungry."""
        if not self.is_alive:
            print(f"👻 {self.name} cannot play. RIP.")
            return

        if self.hunger < 20:
            print(f"\n🚫 {self.name} is too hungry to play! Feed them first.")
            return

        print(f"\n🎾 You play fetch with {self.name}...")
        time.sleep(1)
        
        self.happiness += 20
        self.hunger -= 10  # Playing burns energy!
        
        if self.happiness > 100: self.happiness = 100
        
        print(f"🎉 {self.name} had fun! Happiness is now {self.happiness}/100.")

    def get_status(self):
        """Returns a formatted status report."""
        mood = "Neutral"
        if self.happiness > 80: mood = "Happy 😄"
        elif self.happiness < 30: mood = "Sad 😢"
        elif self.hunger < 20: mood = "Hangry 😠"

        print(f"\n📊 --- {self.name}'s Status ---")
        print(f"   Species: {self.species}")
        print(f"   Hunger:    {self.hunger}/100")
        print(f"   Happiness: {self.happiness}/100")
        print(f"   Mood:      {mood}")
        print("--------------------------")

    def check_health(self):
        """Checks if the pet has died of starvation."""
        if self.hunger <= 0:
            print(f"\n💀 Oh no! {self.name} has starved to death...")
            self.is_alive = False
        elif self.happiness <= 0:
            print(f"\n💔 {self.name} ran away because they were too sad.")
            self.is_alive = False

# --- Main Game Loop ---
def main():
    print("=== 🐾 WELCOME TO PET SIMULATOR 🐾 ===")
    p_name = input("Name your pet: ")
    p_species = input("What species is it? (Cat/Dog/Dragon): ")
    
    # Create the Object (Instance of the Class)
    my_pet = Pet(p_name, p_species)

    while my_pet.is_alive:
        print(f"\nWhat would you like to do with {my_pet.name}?")
        print("1. 🍖 Feed")
        print("2. 🎾 Play")
        print("3. 📊 Check Status")
        print("4. 🚪 Quit")
        
        choice = input("Choice (1-4): ")
        
        if choice == '1':
            my_pet.feed()
        elif choice == '2':
            my_pet.play()
        elif choice == '3':
            my_pet.get_status()
        elif choice == '4':
            print("Bye! 👋")
            break
        else:
            print("Invalid choice.")
        
        # Check if pet survived the turn
        my_pet.check_health()
        
        # Random event: Pet gets slightly hungrier over time
        if random.random() < 0.3:
            my_pet.hunger -= 5
            print(f"\n(Time passes... {my_pet.name} gets a bit hungry)")

if __name__ == "__main__":
    main()