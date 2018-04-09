class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.is_alive = True
        self.hunger = 100
        self.thirst = 100
        self.hygine = 100
        self.energy = 100
        

    def eat(self):
        if self.is_alive:
            print(self.name + ": ''Nom Nom Nom...''")
            self.hunger += 15
            self.energy -= 5
            print(self.name + "hunger: " + str(self.hunger) + " energy: " + str(self.energy))
        else:
            print("Ded Bois don't eat.")
        

    def sleep(self):
        if self.is_alive:
            print(self.name + ": ''zzzzzzzzzzzzzz...''")
            self.energy += 15
            self.hunger -= 10
            print(self.name + "energy: " + str(self.energy) + " Hunger: " + str(self.hunger))
        else:
            print(self.name + " is already gettign that GOOOOOD sleep. ;)")

    def play(self):
        if self.is_alive:
            print(self.name + ": ''Yipee!''")
            self.energy -= 10
            self.hunger -= 20
            print(self.name + "energy: " + str(self.energy) + " Hunger: " + str(self.hunger))
        else:
            print(self.name + " is playing in heaven.")

    def growl(self):
        if self.is_alive:
            print(self.name + ": ''GRRRRrrr!!!''")
            
        else:
            print("Ded Bois don't Bark....")

    def love(self):
        if self.is_alive:
            self.energy -= 35
            print(self.name + ": ''peeper purrr purrr''")
            print(self.name + " Hunger: " + str(self.hunger))
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

    
pet1 = Pet("Manuela")
pet2 = Pet("Blato")
pet3 = Pet("Wakasa")
pet4 = Pet("Kassie")
pet5 = Pet("Peter")
pet6 = Pet("Luna")
