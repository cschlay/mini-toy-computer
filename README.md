# Mini Toy Computer

The project is based on [RASP-Machine](https://en.wikipedia.org/wiki/Random-access_stored-program_machine).
This is also a project to learning more about computers and algorithms.

The machine can already process the basic instructions described in Wikipedia.

## Use Instruction
1. Start the computer by running ```src/main.py```. It should just work.
2. You can then run the programs stored at ```src/programs```.
The demo program is not okay atm.

## Terminal Commands
Programs should be stored at directory ``src/programs``.
The compiled programs are stored at ``src/programs/compiled``.

When we say "disk" we mean an ``*.sqlite3`` database.
It does not work like a real disk.

| Command                     | Action |
| --------------------------- | ------ |
| ``COMPILE <program_name>`` | Compiles a program such that is runnable. |
| ``RUNLOC <program_name>`` | Runs a compiled program.|

## Supported Instructions
The 8-instruction base set according to [Wikipedia](https://en.wikipedia.org/wiki/Random-access_stored-program_machine)
is an universal turing machine which implies that you should be able to do anything computable.
The problem is just that it is not very obvious.

You can extend the instruction set by putting them in ```compiler/extra_instructions```.

The set ```{ADD, BPA, CPY (STORE), HALT, LDA (LOAD), SUB, PRINT, READ,}``` is described [here](https://en.wikipedia.org/wiki/Random-access_stored-program_machine#RASP_program-instruction_set_of_Cook_and_Reckhow_(1973)).
The instruction format in our toy computer is ```<INSTRUCTION> <ARGUMENT>```.
Each part is separated by spaces and comment begins with ```#``` character followed by space.

***Example***:
```
# Setting value 8 to register 3.

LDA   0000_1000  # Set 8 to accumulator.
CPY   0000_0011  # Copying the value from accumulator to register 3.
PRINT 0000_0011  # Print the value of register 3.
```

## Limits
According to the processor_test.py it seems like we get incorrect results when the numbers are outside the range of [-128, 127].