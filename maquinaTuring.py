class TuringMachine:
    def __init__(self, tape, transitions, initial_state, accepting_states):
        self.tape = list(tape)
        self.transitions = transitions
        self.state = initial_state
        self.head = 0
        self.accepting_states = accepting_states

    def step(self):
        symbol = self.tape[self.head]
        action = self.transitions.get((self.state, symbol))
        
        if action:
            new_symbol, move, new_state = action
            self.tape[self.head] = new_symbol
            self.head += 1 if move == 'R' else -1
            self.state = new_state

            if self.head < 0:
                self.tape.insert(0, '_')
                self.head = 0
            elif self.head >= len(self.tape):
                self.tape.append('_')
        else:
            print("Nenhuma transição possível; a máquina parou.")

    def run(self):
        while self.state not in self.accepting_states:
            self.step()
            print("Fita:", ''.join(self.tape), "Estado:", self.state)

tape = "101"
transitions = {
    ('q0', '1'): ('_', 'R', 'q1'),
    ('q1', '0'): ('_', 'R', 'q2'),
}
accepting_states = {'q2'}

tm = TuringMachine(tape, transitions, 'q0', accepting_states)
tm.run()
