# Copyright (c) 2018 - C. H. Lay
# MIT License https://en.wikipedia.org/wiki/MIT_License

from BinaryNumber import BinaryNumber
from Register import Register


class Processor:
    """
    Emulates a processor for RASP-Machine.
    https://en.wikipedia.org/wiki/Random-access_stored-program_machine
    """
    REGISTER_COUNT = 8

    def __init__(self):
        """
        Constructs a new virtual processor with pre-defined register count.
        Register 0 is used as accumulator.
        Register 1 is used as instruction counter.
        The rest are freely usable.
        """
        self.registers: list = [Register] * Processor.REGISTER_COUNT
        self.instruction_memory: list = []

    def load(self, immediate: BinaryNumber):
        """
        Instruction: LDA, I
        Load a value to the accumulator.
        """
        self.registers[0] = immediate

    def add(self, immediate: BinaryNumber):
        """
        Instruction: ADD, I
        Performs addition to value in the accumulator such that accumulator += I.
        """
        A: BinaryNumber = self.accumulator
        B: BinaryNumber = immediate
        C: BinaryNumber = BinaryNumber()

        carry = 0
        for i in reversed(range(BinaryNumber.LENGTH)):
            if A[i] + B[i] + carry == 3:
                carry = 1
                C[i] = 1
            elif A[i] + B[i] + carry == 2:
                carry = 1
            else:
                C[i] = A[i] + B[i] + carry
                carry = 0

        self.registers[0] = C

        if carry == 1:
            print("OVERFLOW")

    def branch(self, address: int):
        """
        Instruction: BPA, A
        Sets the instruction counter to value A if the accumulator is greater than 0.
        """
        if self.registers[0].decimal() > 0:
            self.registers[1] = address     # Set the instruction counter to address A.

    def read(self):
        pass

    def store(self):
        pass

    def substract(self):
        pass

    def print(self, address: int):
        print(self.registers[address])
