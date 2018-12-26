from tests.randomizer import random_binary_number

CASES = 5

print("POSITIVE NUMBERS TEST")
for x in range(CASES):
    A = random_binary_number()
    A[0] = 0
    print(f"{str(A)} = {A.decimal()}")

print("NEGATIVE NUMBERS TEST")
for x in range(CASES):
    A = random_binary_number()
    A[0] = 1
    print(f"{str(A)} = {A.decimal()}")
