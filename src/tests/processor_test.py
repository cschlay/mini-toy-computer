# Copyright (c) 2018 - C. H. Lay
# MIT License https://en.wikipedia.org/wiki/MIT_License
from Processor import Processor
from tests.randomizer import random_binary_number

processor = Processor()


def addition_test():
    """
    Tests processors addition function.
    """
    cases = 1000
    passed = 0
    for x in range(cases):
        A = random_binary_number()
        B = random_binary_number()

        processor.load(A)
        processor.add(B)

        if processor.registers[Processor.ACCUMULATOR].decimal() == A.decimal() + B.decimal():
            passed += 1

    print(f"ADDITION TEST: {passed}/{cases}")


addition_test()
