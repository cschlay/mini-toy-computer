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
        print("[*] To run a program write the program's filename.")
        print("[*] To compile a program: COMPILE program_filename\n")
        print("---")
