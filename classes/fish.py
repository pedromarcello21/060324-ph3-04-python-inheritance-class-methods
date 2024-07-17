class Fish:

    all_fish = []

    @classmethod
    def num_fish(cls):
        return len(cls.all_fish)
    
    @classmethod
    def all_fish_names(cls):
        fish_names = []
        for i in cls.all_fish:
            fish_names.append(i.name)
        return fish_names
    
    @classmethod
    def average_length(cls):
        length_sum = 0
        for i in cls.all_fish:
            length_sum += i.length_in_inches
        return length_sum/len(cls.all_fish)

    def __init__(self, name, length_in_inches):
        self.name = name
        self.length_in_inches = length_in_inches
        Fish.all_fish.append(self)

    def __repr__(self):
        return f"Fish(name={self.name}, length_in_inches={self.length_in_inches})"

    def make_bubbles(self):
        return "bloop bloop"
