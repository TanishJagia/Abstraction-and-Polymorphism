from abc import ABC, abstractmethod
class ABSclass(ABC):
    def print(self, x):
        print("Passed value: ", x)

    @abstractmethod
    def task(self):
        pass
class test_class(ABSclass):
    def task(self):
        print("We are inside test_class task.")
test_obj = test_class()
test_obj.task()
test_obj.print(5)
