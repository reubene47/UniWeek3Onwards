class Human():
    MAX_ENERGY = 100

    def __init__(self, name):
        self.name = name
        self.age = 0
        self.energy = Human.MAX_ENERGY

    def display(self):
        return(f"I am {self.name}")