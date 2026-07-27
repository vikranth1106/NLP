# DFA Simulator

# States
states = ['q0', 'q1', 'q2']

# Transition Table
transitions = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q0',

    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q2',

    ('q2', 'a'): 'q1',
    ('q2', 'b'): 'q0'
}

start_state = 'q0'
final_states = ['q2']

string = input("Enter Input String: ")

current = start_state
path = [current]

valid = True

for ch in string:
    if (current, ch) in transitions:
        current = transitions[(current, ch)]
        path.append(current)
    else:
        valid = False
        break

print("\nTransition Path:")
print(" → ".join(path))

if valid and current in final_states:
    print("Accepted")
else:
    print("Rejected")