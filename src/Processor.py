# Copyright (c) 2018 - C. H. Lay
# MIT License https://en.wikipedia.org/wiki/MIT_License

from BinaryNumber import BinaryNumber
from Register import Register


class Processor:
    def __init__(self):
        self.accumulator: BinaryNumber
        self.memory: list = [Register] * 8
        self.instruction_memory: list = []

    def load(self, immediate: BinaryNumber):
        self.accumulator = immediate

    def add(self, immediate: BinaryNumber):
        """
        Could be thought as accumulator = accumulator + immediate.

        :param immediate:
        :return:
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

        self.accumulator = C

        if carry == 1:
            print("OVERFLOW")
