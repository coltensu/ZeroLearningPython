from time import sleep


class Student:
    __slots__ = ['_name', '_age', '_time']

    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._time = 0

    def study(self, time):
        self._time += time
        sleep(time)

    def status(self):
        print(self._name, self._age, self._time)

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def time(self):
        return self._time

    @age.setter
    def age(self, age):
        self._age = age


if __name__ == '__main__':
    fish = Student('fish', 18)
    fish.study(3)
    fish.status()
    print('name:', fish.name)
    fish.age += 1
    fish.status()
