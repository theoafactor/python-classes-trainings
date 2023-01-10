class User():

    #the constructor method
    def __init__(self, firstname):
        print("This is the constructor method")
        self.firstname = firstname

    #the sleep method
    def sleep(self):
        print("I am sleeping")

    #the run method
    def run(self):
        print("I am running")

    #the walk method
    def walk(self):
        print("I am walking")

#create an object from User class
#person = User('James')

african_person = User('Kunle' )
asian_person = User('Kan Lao')

print(african_person.firstname)
print(asian_person.firstname)

# person.sleep()
# person.run()
# person.walk()