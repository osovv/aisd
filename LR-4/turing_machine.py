
class Tape:

    blank_symbol = " "

    def __init__(self,
                 tape_string = ""):
        self.tape = dict((enumerate(tape_string)))

    def __str__(self):
        return ''.join(self.tape.values())

    def __getitem__(self,index):
        if index in self.tape:
            return self.tape[index]
        else:
            return Tape.blank_symbol

    def __setitem__(self, pos, char):
        self.tape[pos] = char


class TuringMachine(object):

    def __init__(self,
                 tape = "",
                 blank_symbol = " ",
                 initial_state = "",
                 final_states = None,
                 transition_function = None):
        self.tape = Tape(tape)
        self.head_position = 0
        self.blank_symbol = blank_symbol
        self.current_state = initial_state
        self.transition_function = transition_function or {}
        self.final_states = set(final_states) or set()

    def get_tape(self):
        return str(self.tape)

    def step(self):
        char_under_head = self.tape[self.head_position]
        x = (self.current_state, char_under_head)
        if x in self.transition_function:
            y = self.transition_function[x]
            self.tape[self.head_position] = y[1]
            if y[2] == "R":
                self.head_position += 1
            elif y[2] == "L":
                self.head_position -= 1
            self.current_state = y[0]

    def final(self):
        if self.current_state in self.final_states:
            return True
        else:
            return False

    def run(self):
        while not self.final():
            self.step()


if __name__ == "__main__":
    tape = "||| "
    initial_state = "init"
    accepting_states = ["final"]
    transition_function = {
        ("init", "|"):("init", "|", "R"),
        ("init", " "):("pre-final", " ", "L"),
        ("pre-final", "|"):("final", " ", "R")
    }
    final_states = {"final"}

    t = TuringMachine(
        tape=tape,
        initial_state=initial_state,
        final_states=final_states,
        transition_function=transition_function
    )

    print("Input on Tape:")
    print(t.get_tape())

    t.run()

    print("Result:")
    print(t.get_tape())
