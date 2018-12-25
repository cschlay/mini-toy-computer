from computer.DiskManager import DiskManager
from computer.Processor import Processor

import sys, pygame


class Computer:
    """
    A very default model of a computer: 1 processor and 1 disk.
    """
    def __init__(self, disk_location: str):
        pygame.init()
        self.disk = DiskManager(disk_location)
        self.processor = Processor()
        self.display = pygame.display.set_mode((600, 400))

    def boot(self):
        self.display.fill((158, 74, 61))
        pygame.display.set_caption('Mini Toy Computer - CscHLay Laboratories')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            pygame.display.flip()
