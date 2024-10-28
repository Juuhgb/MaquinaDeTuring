# Máquina de Turing

Este projeto implementa uma Máquina de Turing simples em Python. A máquina processa uma fita de entrada e faz transições com base nas regras fornecidas.

## Estrutura do Código

- `TuringMachine`: Classe que define a máquina de Turing.
  - `__init__(self, tape, transitions, initial_state, accepting_states)`: Inicializa a máquina com a fita, transições, estado inicial e estados de aceitação.
  - `step(self)`: Executa um passo da máquina, atualizando a fita, movendo a cabeça e mudando o estado.
  - `run(self)`: Executa a máquina até alcançar um estado de aceitação.

## Exemplo de Uso

```python
tape = "101"
transitions = {
    ('q0', '1'): ('_', 'R', 'q1'),
    ('q1', '0'): ('_', 'R', 'q2'),
}
accepting_states = {'q2'}

tm = TuringMachine(tape, transitions, 'q0', accepting_states)
tm.run()
