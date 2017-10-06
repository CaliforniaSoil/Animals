class animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health = self.health - 1
        return self
    def run(self):
        self.health = self.health - 5
        return self
    def displayHealth(self):
        print "Name:", self.name
        if self.name == "Dragon":
            print "I am a Dragon"
        print "Health:", self.health
animal1 = animal("Aminal")
animal1.walk().run().displayHealth()
class dog(animal):
    def __init__(self, name):
        self.name = name
        self.health = 150
    def pet(self):
        self.health = self.health +5
        return self
dog1 = dog("Dog")
dog1.walk().run().walk().pet().displayHealth()
class dragon(animal):
    def __init__(self, name):
        self.name = name
        self.health = 170
    def fly(self):
        self.health = self.health - 10
        return self
dragon1 = dragon("Dragon")
dragon1.fly().fly().displayHealth()
class cat(animal):
    def __init__(self, name):
        self.name = name
        self.health = 9000
    def purr(self):
        self.health = self.health + 25
        return self
cat1 = cat("Leo")
cat1.purr().purr().walk().walk().walk().walk().displayHealth()