"""
Module: mod_three
This module contains the implementation of a Finite State Machine (FSM) 
to determine the remainder of a binary number when divided by three.
"""

class ModThreeFSM:
    def __init__(self):
        # Define the transition function
        self.transitions = {
            'S0': {'0': 'S0', '1': 'S1'},
            'S1': {'0': 'S2', '1': 'S0'},
            'S2': {'0': 'S1', '1': 'S2'}
        }
        # Initial state
        self.current_state = 'S0'
    
    def process_bit(self, bit):
        # Transition to the next state based on the input bit
        self.current_state = self.transitions[self.current_state][bit]
    
    def get_remainder(self):
        # Map the final state to the corresponding remainder
        state_to_remainder = {'S0': 0, 'S1': 1, 'S2': 2}
        return state_to_remainder[self.current_state]

def mod_three(binary_string):
    if not isinstance(binary_string, str):
        raise ValueError("Input must be a string.")
    if len(binary_string) == 0:
        raise ValueError("Input must be a non-empty string.")
    if not all(bit in '01' for bit in binary_string):
        raise ValueError("Input string must contain only '0's and '1's.")

    fsm = ModThreeFSM()
    for bit in binary_string:
        fsm.process_bit(bit)
    return fsm.get_remainder()
