# Copyright (c) 2018 - C. H. Lay
# MIT License https://en.wikipedia.org/wiki/MIT_License

from BinaryNumber import BinaryNumber


class Register:
    """
    Represents a register of a computation system.
    """

    def __init__(self):
        """
        Constructs a new default-length register.
        """
        self.data: BinaryNumber = BinaryNumber()

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value
