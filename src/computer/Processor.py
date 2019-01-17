# Copyright (c) 2018 - C. H. Lay
# MIT License https://en.wikipedia.org/wiki/MIT_License
from compiler.Compiler import Compiler
from computer.BinaryNumber import BinaryNumber


class Processor:
    """
    Emulates a processor for RASP-Machine.
    https://en.wikipedia.org/wiki/Random-access_stored-program_machine
    """
    REGISTER_COUNT = 8
    ACCUMULATOR = 0

    def __init__(self):
        """
        Constructs a new virtual processor with pre-defined register count.
        Register 0 is used as accumulator.
        The rest are freely usable.
        """
        self.registers: list = [BinaryNumber] * Processor.REGISTER_COUNT
        self.instruction_memory: list = []
        self.instruction_counter: int = 0

    def add(self, address: int):
        """
        Instruction: ADD, R
        Performs addition to value in the accumulator such that accumulator += register_R.
        """
        A: BinaryNumber = self.registers[Processor.ACCUMULATOR]
        B: BinaryNumber = self.registers[address]
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

        self.registers[Processor.ACCUMULATOR] = C

        if carry == 1:
            print(f"OVERFLOW {A} + {B}")

    def branch(self, address: int):
        """
        Instruction: BPA, A
        Sets the instruction counter to value A if the accumulator is greater than 0.
        """
        if self.registers[Processor.ACCUMULATOR].decimal() > 0:
            self.instruction_counter = address     # Set the instruction counter to address A.

    def copy(self, address: int):
        """
        Instruction: CPY, A
        Copies accumulator data to register A.
        """
        self.registers[address] = self.registers[Processor.ACCUMULATOR].copy()

    def load(self, immediate: BinaryNumber):
        """
        Instruction: LDA, I
        Load a value to the accumulator.
        """
        self.registers[0] = immediate

    def read(self, address: int):
        """
        Instruction: READ, A
        Read an value into register A.
        Currently only supporting bare binary inputs.
        """
        value: str = input("prompt")

        input_ok = True
        for char in value:
            input_ok = (char in {'0', '1'})

        if input_ok:
            self.registers[address] = BinaryNumber(value)
        else:
            print("INCORRECT INPUT")

    def print(self, address: int):
        """
        Instruction: PRINT, A
        Print the contents of register A.
        """
        print(self.registers[address])

    def subtract(self, address: int):
        """
        Instruction: SUB, R
        Performs a subtraction on accumulator such that accumulator -= register_R.
        """
        immediate = self.registers[address].copy()

        # Computing -x (see https://www.nand2tetris.org/course, project 2).
        for i in range(BinaryNumber.LENGTH):
            immediate[i] = 0 if immediate[i] else 1

        # Accumulator to register 1.
        self.copy(1)
        # Value 1 to register 2.
        self.load(BinaryNumber("00000001"))
        self.copy(2)
        # Performing I + 1.
        self.load(immediate)
        self.add(2)
        self.copy(2)

        # Finally subtracting by using addition.
        # Clearing the accumulator
        self.load(BinaryNumber())
        # A - B
        self.add(1)
        self.add(2)

    def load_program(self, program_location: str):
        """
        Loads a program into instruction memory.
        Does not replace the existing ones, it just appends the memory.
        """
        with open(program_location) as program:
            for instruction in program:
                self.instruction_memory.append(instruction.replace('\n', ''))

    def execute(self) -> bool:
        """
        Executes the instructions in the memory.
        Return true if a program is successfully executed.

        https://en.wikipedia.org/wiki/Instruction_cycle
        """
        while self.instruction_counter < len(self.instruction_memory):
            # "Fetching" an instruction.
            instruction: list = self.instruction_memory[
                                    self.instruction_counter].split()

            # For every instruction[0] is the operation and the rest are arguments.
            op: str = instruction[0]

            ar = None
            if len(instruction) == 2:
                ar = instruction[1] if op == "BPA2" else BinaryNumber(instruction[1])

            # Execution phase.
            if op == "LDA":
                self.load(ar)
            elif op == "ADD":
                self.add(ar.decimal())
            elif op == "SUB":
                self.subtract(ar.decimal())
            elif op == "CPY":
                self.copy(ar.decimal())
            elif op == "BPA":
                self.branch(ar.decimal())
                self.instruction_counter -= 1
            elif op == "BPA2":
                # Find the tag.
                i: int = 0

                for x in self.instruction_memory:
                    if x == ar:
                        self.branch(i)
                        print(i)
                    i += 1
            elif op == "READ":
                self.read(ar.decimal())
            elif op == "PRINT":
                self.print(ar.decimal())
            # The instruction is a tag.
            elif "__" in op:
                pass
            # If a command is unknown, we stop the program.
            else:
                self.instruction_counter += len(self.instruction_memory)

            self.instruction_counter += 1

        return True
