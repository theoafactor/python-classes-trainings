class Bird():

    def __init__(self, name, color):
        self.name = name 
        self.color = color

    def run(self):
        print(self.name +" is running")

    def layEgg(self, number):
        number = str(number)
        print(self.name + " has layed " + number + " egg(s)")



class FlyingBird(Bird):
    def __init__(self, name, color):
        self.name = name 
        self.color = color
        print("This is the constructor of flyingbird class")

    def run(self):
        print("nothing")
        super().run()

    

class NonFlyingBird(Bird):
    pass


bird = FlyingBird('owl', 'black')
bird.run()





# owl = Bird('owl', 'black')
# ostrich = Bird('ostrich', 'white')


# owl.layEgg(2)
# ostrich.layEgg(10)
