from compiler.Compiler import Compiler
from computer.DiskManager import DiskManager
from computer.Processor import Processor


class Computer:
    """
    A very default model of a computer: 1 processor and 1 disk.
    """
    def __init__(self, disk_location: str):
        self.disk = DiskManager(disk_location)
        self.processor = Processor()

    def boot(self):
        print("'Mini Toy Computer' by CscHLay Laboratories\n")
        print("[*] Switch off the computer: SHUTDOWN")
        print("[*] Compile a program:       COMPILE program_filename")
        print("[*] Run a program:           RUNLOC  program_filename")
        print("\nSee README.md for more commands.\n")
        print("---")
        run = True

        # Emulates a console, note that this is not the operating system.
        while run:
            print('> ', end='')
            command = input().split()

            if command[0] in {"shutdown", "SHUTDOWN"}:
                run = False
            elif command[0] in {"compile", "COMPILE"}:
                compiler = Compiler()
                try:
                    compiler.compile(command[1])
                except IndexError:
                    print("ERROR: Command 'compile' needs a filename.")
            elif command[0] in {"runloc", "RUNLOC"}:
                self.processor.load_program(f"programs/{command[1]}")
                self.processor.execute()
            else:
                print("ERROR: Unknown Command.")
