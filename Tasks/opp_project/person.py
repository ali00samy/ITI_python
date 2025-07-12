class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = min(max(healthRate, 0), 100)

    def sleep(self, hours):
        if hours == 7:
            self.mood = "Happy"
        elif hours < 7:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        else:
            self.healthRate = 50

    def buy(self, items):
        self.money -= 10 * items
