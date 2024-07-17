class Bird:

    all_birds = []

    #Only calling on Bird class
    @classmethod
    def number_of_birds(cls): ##cls can be w/e
        return len(cls.all_birds)

    def __init__(self, name):
        self.name = name
        Bird.all_birds.append(self)

    def __repr__(self):
        return f"Bird(name={self.name})"

    def tweet(self):
        return f"{self.name} is posting all their tweets... I mean X's"
