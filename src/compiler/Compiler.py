from pathlib import Path


class Compiler:
    INSTRUCTION_SET = {
        'ADD', 'SUB', 'MUL',
    }


def process_line(self, line: str) -> [str] or None:
    """
    Pre-processes a line by removing comments and whitespaces.
    Return a line as an array.
    If a line does not have valid instructions, it will return None.
    """
    line_splitted = line.split()
    if line_splitted in Compiler.INSTRUCTION_SET:
        cut_index = 0
        for token in range(len(line_splitted)):
            if token == '#':
                cut_index = token
        return line_splitted[:cut_index]
    else:
        return None
