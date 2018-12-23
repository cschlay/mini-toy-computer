# Copyright (c) 2018 - C. H. Lay
# MIT License https://en.wikipedia.org/wiki/MIT_License


class BinaryNumber:
    """
    Represents a binary number as an array.
    """
    LENGTH = 8

    def __init__(self):
        self.array = [0] * BinaryNumber.LENGTH

    def decimal(self) -> int:
        result: int = 0

        j = BinaryNumber.LENGTH - 1
        i = 0
        while j >= 0:
            if self.array[j] == 1:
                result = result + 2**i
            i = i + 1
            j = j - 1

        return result

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value

    def __str__(self):
        return str(self.array)