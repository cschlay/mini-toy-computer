import os


class Compiler:
    INSTRUCTION_SET = {
        'ADD', 'SUB', 'MUL',
    }

    def __init__(self, root_directory: str = "programs"):
        self.ROOT: str = root_directory
        self.COMPILED = f"{self.ROOT}/compiled"
        if not os.path.exists(self.COMPILED):
            os.makedirs(self.COMPILED)

    def compile(self, file: str):
        try:
            with open(file) as program:
                for line in program:
                    pass
        except:
            print("ERROR: Program not found, did you compile it first?")

def process_line(self, line: str) -> [str] or None:
    """
    Pre-processes a line by removing comments and whitespaces.
    Return a line as an array.
    If a line does not have valid instructions, it will return None.
    """
    line_splitted: list = line.split()
    if line_splitted[0] in Compiler.INSTRUCTION_SET:
        cut_index = 0
        for token in range(len(line_splitted)):
            if token == '#':
                cut_index = token
        return line_splitted[:cut_index]
    else:
        return None
