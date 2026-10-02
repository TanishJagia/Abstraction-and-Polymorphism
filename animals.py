from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Monkey(Animal):
    def move(self):
        print("I can climb trees and swing from branches.")
class Snake(Animal):
    def move(self):
        print("I can slither on the ground.")
class Dog(Animal):
    def move(self):
        print("I can run and walk on 4 legs like most animals.")

obj_monkey = Monkey()
obj_snake = Snake()
obj_dog = Dog()
for animal in (obj_monkey, obj_snake, obj_dog):
    animal.move()
