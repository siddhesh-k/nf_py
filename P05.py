class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


class Bulldog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight

    def bark(self):
        print("Gruff!")


# Creating an instance of Bulldog
bulldog = Bulldog("Rocky", 2, 23)
print(bulldog.name)  # Output: Rocky
print(bulldog.age)  # Output: 2
print(bulldog.weight)  # Output: 23
bulldog.bark()  # Output: Gruff!
bulldog1 = Bulldog("timmy",5,23)
print(bulldog1 == bulldog)

class Doggie:
    def __init__(self, name, age):
        self.name = name  # public attribute
        self.__age = age  # private attribute
    def __str__(self):
        return f"{self.name} is a good doggie"
    def get_age(self):  # public method
        return self.__age
    def set_age(self, age):  # public method
        if age > 0:
            self.__age = age



my_dog = Doggie("Buddy", 3)
my_dog2= Doggie("Jones",4)
# print(my_dog.name)           # Output: Buddy
# print(my_dog)           # Output: Buddy
# print(my_dog.get_age())      # Output: 3
# my_dog.set_age(4)
# print(my_dog.get_age())
print(my_dog)
my_dog.name="BuddyNew"
print(my_dog)
print(my_dog2)
