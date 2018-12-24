# Copyright (c) 2018 - C. H. Lay
# MIT License https://en.wikipedia.org/wiki/MIT_License
# This test is written to be manually verified.
from tests.randomizer import random_binary_number

CASES = 5

print("POSITIVE NUMBERS TEST")
for x in range(CASES):
    A = random_binary_number()
    print(f"{str(A)} = {A.decimal()}")

print("NEGATIVE NUMBERS TEST")
for x in range(CASES):
    A = random_binary_number()
    A[0] = 1
    print(f"{str(A)} = {A.decimal()}")
