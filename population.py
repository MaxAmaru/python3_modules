
class person():
    def __init__(self, name, gender, city):
        if (city.capacity > city.population):
            self.name = name
            self.gender = gender
            self.age = 1
            self.city = city
            print("------------------------------------------------")
            print("Bob: name: " + name + " gender: " + gender + " age: " + str(self.age) + " home: " + city.name)
            city.population += 1
            print(city.name + "'s population is now " + str(city.population) + ".")
            print("------------------------------------------------")
        else:
            print("")
            print("No room left in city!")

    def setAge(self, age):
        self.age = age
        print(self.name + "'s age has been set to " + str(self.age))

    def changeName(self, newName):
        if (self.age >= 18):
            print(self.name + " changed their name to " + newName + ".")
            self.name = newName
        else:
            print(self.name + " is not old enough to change their name!")

class city():
    def __init__(self, name, capacity):
        self.name = name
        self.population = 0
        self.capacity = capacity
        print("New city named " + name + " has been created with a capacity of " + str(capacity) + ". So far the population is " + str(self.population) + ".")
    def extend(self, size):
        self.capacity += size
