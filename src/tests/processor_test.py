# Copyright (c) 2018 - C. H. Lay
# MIT License https://en.wikipedia.org/wiki/MIT_License
from computer.Processor import Processor
from tests.randomizer import random_binary_number

processor = Processor()


def addition_test():
    """
    Tests processor's addition function.
    """
    cases = 5
    passed = 0
    for x in range(cases):
        A = random_binary_number()
        B = random_binary_number()
        C = A.decimal() + B.decimal()

        print(f"A = {str(A)} = {A.decimal()}")
        print(f"B = {str(B)} = {B.decimal()}")
        processor.load(A)
        processor.add(B)
        print(f"C = {processor.registers[Processor.ACCUMULATOR]} = {C}")

        if processor.registers[Processor.ACCUMULATOR].decimal() == C:
            passed += 1
            print("PASSED")
        else:
            print("FAILED")
        print("---")

    print(f"ADDITION TEST: {passed}/{cases}")


def subtraction_test():
    """
    Tests processor's subtraction function
    """
    cases = 5
    passed = 0
    for x in range(cases):
        A = random_binary_number()
        B = random_binary_number()
        C = A.decimal() - B.decimal()

        print("--")
        print(f"A = { A.decimal() }, B = { B.decimal() }")
        processor.load(A)
        processor.subtract(B)
        print(f"A - B = {processor.registers[Processor.ACCUMULATOR].decimal()} == {C}")
        print(processor.registers[Processor.ACCUMULATOR].decimal() == C)

        if processor.registers[Processor.ACCUMULATOR].decimal() == C:
            passed += 1

    print(f"SUBTRATION TEST: {passed}/{cases}")


def compiled_source_test():
    """
    Tests whether the processor can process compiled sources from text files.
    """
    processor.load_program("test_program.compiled")
    message = "COMPILED SOURCE TEST: - {} -"
    if processor.execute():
        print(message.format("PASSED"))
    else:
        print(message.format("FAILED"))


addition_test()
subtraction_test()
compiled_source_test()