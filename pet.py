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

        
    
pet1 = Pet("Manuela")
pet2 = Pet("Blato")
pet3 = Pet("Wakasa")
pet4 = Pet("Kassie")
pet5 = Pet("Peter")
pet6 = Pet("Luna")
