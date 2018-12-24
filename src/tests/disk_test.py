from BinaryNumber import BinaryNumber
from computer.DiskManager import DiskManager
from tests.randomizer import random_binary_number

disk = DiskManager("testing_disk.sqlite3")

print("DISK READ TEST =")
print("\nReading an empty address.")
print("Expected: " + str(BinaryNumber()))
print("Result:   " + str(disk.read(0)))

i = 1
while i <= 5:
    data = random_binary_number()
    print(f"\nWriting to address {i}.")
    disk.write(i, data)
    print(f"Expected: {data}")
    print("Result:   " + str(disk.read(i)))
    i = i + 1
