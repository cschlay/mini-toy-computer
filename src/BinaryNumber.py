# Copyright (c) 2018 - C. H. Lay
# MIT License https://en.wikipedia.org/wiki/MIT_License


class BinaryNumber:
    """
    Represents a binary number as an array.
    """
    LENGTH = 8

    def __init__(self):
        self.array = [0] * BinaryNumber.LENGTH

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value
