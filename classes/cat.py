class Cat:

    def __init__(self, name, rested, lives_remaining=9):
        self.name = name
        self.rested = rested
        self.lives_remaining = lives_remaining

    def __repr__(self):
        return f"Cat(name={self.name}, rested={self.rested}, lives_remaining={self.lives_remaining})"

    def make_sound(self):
        return "generic mammal sound"

    def sleep(self):
        self.rested = True

    def run_around(self):
        self.rested = False