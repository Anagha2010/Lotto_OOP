# import from random module
from random import randint

# class definition
class Lotto:
    # class variable
    obj_count = 0

    # class constructor
    def __init__(self):
        self.__lotto_set = set()
        Lotto.obj_count += 1

    # getter method for lotto set
    def get_lotto(self):
        return self.__lotto_set

    # setter method for lotto set
    def set_lotto(self):
        # loop generates a unique set of 6 numbers in the range 1 to 50, both inclusive
        while len(self.__lotto_set) < 6:
            self.__lotto_set.add(randint(1, 50))
