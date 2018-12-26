import os


class Compiler:
    """
    Makes a program executable.
    """
    INSTRUCTION_SET = {"ADD", "BPA", "CPY", "HALT", "LDA", "PRINT", "READ", "SUB"}
    # The instructions that are build from elementary instructions and stored in compiler/extended_instructions.
    EXTENDED_INSTRUCTIONS = {}

    def __init__(self, root_directory: str = "programs"):
        self.ROOT: str = root_directory
        self.COMPILED = f"{self.ROOT}/compiled"
        if not os.path.exists(self.COMPILED):
            os.makedirs(self.COMPILED)

    def compile(self, file: str):
        """
        Compiles a program such that it can be run.
        """
        try:
            program = open(f"{self.ROOT}/{file}", 'r')

            executable = None
            try:
                executable = open(f"{self.COMPILED}/{file}", 'x')
            except FileExistsError:
                executable = open(f"{self.COMPILED}/{file}", 'w')

            # Process the lines and write them if possible.
            for line in program:
                processed_line: str = process_line(line)
                if processed_line is not None:
                    executable.write(processed_line)

            program.close()
            executable.close()
        except FileNotFoundError:
            print("ERROR: Program not found, most likely in wrong directory. Should be at programs/.")


def process_line(line: str) -> [str] or None:
    """
    Pre-processes a line by removing comments and whitespaces.
    Return a line as an array.
    If a line does not have valid instructions, it will return None.
    """
    # Remove comments
    if '#' in line:
        cut = line.find('#')
        line = line[:cut]

    # Formatting the string.
    line = line.replace('\n', '').replace('_', '').strip()

    if len(line) >= 1 and line.split()[0] in Compiler.INSTRUCTION_SET or Compiler.EXTENDED_INSTRUCTIONS:
        return line
    else:
        return None