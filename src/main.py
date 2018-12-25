import sys

from computer.Computer import Computer


def main(argv):
    computer = Computer("disk1.sqlite3")
    computer.boot()


if __name__ == "__main__":
    main(sys.argv)
