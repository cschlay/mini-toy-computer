# Mini Toy Computer

The project is based on [RASP-Machine](https://en.wikipedia.org/wiki/Random-access_stored-program_machine).
I use this to practice data structures and algorithms on very low-level.
This is also a project to learn more about computers.

The machine can already process the basic instructions described in Wikipedia.
The compiler is currently missing so, you have to use binary numbers and not comment your code.

## Use Instruction
1. Start the computer by running ```src/main.py```. It should just work.
2. You can then run the programs stored at ```src/programs```.

## Terminal Commands


## Supported Instructions
You can extend the instruction set by putting them in ```compiler/extra_instructions```.

The table described [here](https://en.wikipedia.org/wiki/Random-access_stored-program_machine#RASP_program-instruction_set_of_Cook_and_Reckhow_(1973)).
The instruction format in our toy computer is ```<INSTRUCTION> <ARGUMENT>```.
Each part is separated by spaces and comment begins with ```#``` character followed by space.

***Example***:
```
# Setting value 8 to register 3.

LDA   0000_1000  # Set 8 to accumulator.
CPY   0000_0011  # Copying the value from accumulator to register 3.
PRINT 0000_0011  # Print the value of register 3.
```