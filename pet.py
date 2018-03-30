class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.is_alive = True

    def eat(self):
        if self.is_alive:
            print(self.name + ": ''Nom Nom Nom...''")
        else:
            print("Ded Bois don't eat.")
        

    def sleep(self):
        if self.is_alive:
            print(self.name + ": ''zzzzzzzzzzzzzz...''")
        else:
            print(self.name + " is already gettign that GOOOOOD sleep. ;)")

    def play(self):
        if self.is_alive:
            print(self.name + ": ''Yipee!''")
        else:
            print(self.name + " is playing in heaven.")

    def growl(self):
        if self.is_alive:
            print(self.name + ": ''GRRRRrrr!!!''")
        else:
            print("Ded Bois don't Bark....")

    def love(self):
        if self.is_alive:
            print(self.name + ": ''peeper purrr purrr''")
        else:
            print("You should have loved " + self.name + " while they were alive.") 

    def poop(self):
        if self.is_alive:
            print(self.name + ": ''PPPRRRT..... HEEEEWWWWWWEEEERRRUUUUUM...!''")
        else:
            print("At least you don't have to clean up the... unpleasent mess....")

    def wimper(self):
        if self.is_alive:
            print(self.name + ": ''Heerrm Ruuoom''")
        else:
            print("At least they can't cry in the after life.")

    def tickle(self):
        if self.is_alive:  
            print(self.name + ": ''teeheehee, HAHAHA!''")
        else:
            print("There are no tickles in the afterlife.")

        

    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1

    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"

                  
    def kill(self, other):
        print(self.name + " kills " + other.name + "!")
        other.is_alive = False


    def dance(self, other):
        if self.is_alive and other.is_alive:
            print(self.name + " invited " + other.name + " to dance.")
        else:
            print("Can't dance with the ded.")
''' health bar
#Draw Bar
import pygame

def SingleColorBar(surface,color,x,y,value,maxvalue):
    xx=0
    for hp in range(value):
        pygame.draw.rect(surface, color, (x+xx,y,1,32), 0)
        xx+= value/100'''

'''pet stats'''
ticks = 0
while not done:

    def pet1_hunger():
    def pet1_thirst():
    def pet1_happiness():
    def pet1_stress():
    def pet1_potty():
    def pet1_hygiene():


pet2_hunger = 100
pet2_thirst = 100
pet2_happiness = 100
pet2_stress = 0
pet2_potty = 0
pet2_hygiene = 100


pet3_hunger = 100
pet3_thirst = 100
pet3_happiness = 100
pet3_stress = 0
pet3_potty = 0
pet3_hygiene = 100


pet4_hunger = 100
pet4_thirst = 100
pet4_happiness = 100w
pet4_stress = 0
pet4_potty = 0
pet4_hygiene = 100


pet5_hunger = 100
pet5_thirst = 100
pet5_happiness = 100
pet5_stress = 0
pet5_potty = 0
pet5_hygiene = 100



pet6_hunger = 100
pet6_thirst = 100
pet6_happiness = 100
pet6_stress = 0
pet6_potty = 0
pet6_hygiene = 100

        
    
pet1 = Pet("Manuela")
pet2 = Pet("Blato")
pet3 = Pet("Wakasa")
pet4 = Pet("Kassie")
pet5 = Pet("Peter")
pet6 = Pet("Luna")
