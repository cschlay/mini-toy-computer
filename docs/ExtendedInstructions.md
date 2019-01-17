# Extended Instruction Set

## Multiplication
Multiply the content of accumulator with a value in register r `MUL r`.
We have an example result of a = 4 and b = 5 such that a * b = 4 * 5:
```
LDA 0000_0101   # Load b = 5.
CPY 0000_0011   # Copy b into register 3.

LDA 0000_0100   # Load a = 4.
CPY 0000_0010   # Copy a into register 2.

LDA 00000001    # Load 1 into register 1.
CPY 00000001

# Here begins the MUL r.
__LOOP-MUL__
LDA 0000_0000   # Clear accumulator.
ADD 0000_0001   # Load a.
ADD 0000_0010   # Add a = a + a.
CPY 0000_0010   # Store a.

LDA 0000_0000   # Clear accumulator
ADD 0000_0011   # Load b.
SUB 0000_0001   # Decrement by one.
CPY 0000_0011   # Store b.
BPA __LOOP-MUL__    # Goto 
```