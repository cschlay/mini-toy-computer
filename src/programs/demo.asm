# This is a demo program.
# There is something wrong with MUL.

LDA 0000_0010 # Load value 2 to accumulator
CPY 0000_0011 # Copy 2 to r3.
LDA 0000_1000 # Load value 8 to accumulator.
MUL 0000_0011 # Perform 2 * 8

# This should print 0001 0000
PRINT 0000_0000