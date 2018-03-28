class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0

    def eat(self):
        print("Nom Nom Nom...")

    def sleep(self):
        print("zzzzzzzzzzzzzz...")

    def play(self):
        print("Yipee!")

    def growl(self):
        print("GRRRRrrr!!!")

    def love(self):
        print("peeper purrr purrr")

    def poop(self):
        print("PPPRRRT..... HEEEEWWWWWWEEEERRRUUUUUM...!")

    def wimper(self):
        print("Heerrm Ruuoom")

    def tickle(self):
        print("teeheehee, HAHAHA!")

        

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
    
    
pet1 = Pet("Manuela")
pet2 = Pet("Blato")
pet3 = Pet("Wakasa")
pet4 = Pet("Kassie")
pet5 = Pet("Peter")
pet6 = Pet("Luna")
