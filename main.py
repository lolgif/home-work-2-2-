class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f"{self.nickname} has the superpower of {self.superpower} and {self.health_points} health points."

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero(name="Брюс Уэйн", nickname="Бэтмэн", superpower="Intellect", health_points=100,
                 catchphrase="I am Batman!")

print(hero.get_name())
hero.double_health()
print(hero)
print(len(hero))
