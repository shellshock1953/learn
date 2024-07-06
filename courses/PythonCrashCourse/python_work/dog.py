class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")

my_dog = Dog('Willie', 6)
print(f"Dog: {my_dog.name}")
my_dog.sit()

your_dog = Dog('Lucy', 3)
print(f"Your dog name is {your_dog.name}, age {your_dog.age}")

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name: {self.restaurant_name}, Cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")


veranda = Restaurant('Veranda', 'bbq')
veranda.describe_restaurant()
veranda.open_restaurant()

class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"first_name: {self.first_name}, last_name: {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name}")

orlando = User('Orlando', 'Groom')
orlando.describe_user()
orlando.greet_user()

