# imports

class Pattern:
    def __init__(self, instructions: dict):
        self.instructions = instructions

    def add_instruction(self, instruction: tuple):
        raise NotImplementedError()

    def remove_instruction(self, index: int):
        raise NotImplementedError()


def blank_pattern():
    return Pattern({})

def load_pattern():
    raise NotImplementedError()