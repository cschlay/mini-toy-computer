# Copyright (c) 2018 - C. H. Lay
# MIT License https://en.wikipedia.org/wiki/MIT_License
from random import randint

from computer.BinaryNumber import BinaryNumber


def random_binary_number() -> BinaryNumber:
    """
    Returns a random BinaryNumber.
    :return:
    """
    result: BinaryNumber = BinaryNumber()

    i = BinaryNumber.LENGTH - 1
    while i > 0:
        result[i] = randint(0, 1)
        i = i - 1

    return result
