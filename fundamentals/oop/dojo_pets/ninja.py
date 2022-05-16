from dojo_pet import Pet

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        print(f"Took {self.pet.name} to the dog park")
        return self

    def feed(self):

        if(len(self.pet_food) > 0):
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}")
            self.pet.eat()
        else:
            print("Oops! We are out of pet food!")
        return self

    def bathe(self):
        self.pet.noise()
        return self

# class Pet:
#     def __init__(self, name, type, tricks, pet_noise, health = 100, energy = 75):
#         self.name = name
#         self.type = type
#         self.tricks = tricks
#         self.health = health
#         self.energy = energy
#         self.pet_noise = pet_noise

#     def sleep(self):
#         self.energy += 25
#         return self

#     def eat(self):
#         self.energy += 5
#         self.health += 10
#         return self

#     def play(self):
#         self.health += 5
#         return self

#     def noise(self):
#         print(self.pet_noise)

my_treats = ['Bone','Chocolate','Tears of my enemies']
my_pet_food = ["Steak", "Chicken"]

Stevie = Pet("Stevie", "Dog", ["Paw", "Lay Down"], "Stevie barks")

JP = Ninja("JP", "Pacheco", my_treats, my_pet_food, Stevie)

JP.walk()
JP.feed()
JP.bathe()