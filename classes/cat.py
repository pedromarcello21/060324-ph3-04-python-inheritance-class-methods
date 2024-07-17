from classes.mammal import Mammal

class Cat(Mammal):

    def __init__(self, name, rested=True, lives_remaining=9):
        super().__init__(name=name)

    def __repr__(self):
        return f"Cat(name={self.name})"
    
    def make_sound(self):
        return "meoww"