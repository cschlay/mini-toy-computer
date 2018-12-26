# Copyright (c) 2018 - C. H. Lay
# MIT License https://en.wikipedia.org/wiki/MIT_License
from computer.Processor import Processor
from tests.randomizer import random_binary_number

processor = Processor()

f = open("processor_test_results.txt", 'w')

CASES = 10

f.write("== ADDITION TEST ==\n")
addition_passed = 0
for i in range(CASES):
    A = random_binary_number()
    B = random_binary_number()

    processor.load(B)   # Setting B to register 1
    processor.copy(1)
    processor.load(A)   # Loading A to accumulator.
    processor.add(1)    # Performing A + B.
    C = processor.registers[Processor.ACCUMULATOR]

    f.write(f"A: {A} = {A.decimal()}\n")
    f.write(f"B: {B} = {B.decimal()}\n")
    f.write(f"+: {C} = {C.decimal()}\n")

    if C.decimal() == (A.decimal() + B.decimal()):
        f.write("PASSED\n\n")
        addition_passed += 1
    else:
        f.write("FAILED\n\n")

f.write("== SUBTRACTION TEST ==\n")
subtraction_passed = 0
for i in range(CASES):
    A = random_binary_number()
    B = random_binary_number()

    processor.load(B)        # Setting B to register 3
    processor.copy(3)
    processor.load(A)        # Loading A to accumulator.
    processor.subtract(3)    # Performing A - B.
    C = processor.registers[Processor.ACCUMULATOR]

    f.write(f"A: {A} = {A.decimal()}\n")
    f.write(f"B: {B} = {B.decimal()}\n")
    f.write(f"-: {C} = {C.decimal()}\n")

    if C.decimal() == (A.decimal() - B.decimal()):
        f.write("PASSED\n\n")
        subtraction_passed += 1
    else:
        f.write("FAILED\n\n")

f.write(f"ADDITION: {addition_passed}/{CASES}\n")
f.write(f"SUBTRACTION: {subtraction_passed}/{CASES}")
f.close()