
initial_state = [1.0,0.0]

transition_matrix = [
     [0.2,0.8],
     [0.4,0.6]
]
current_state = initial_state
new_state = [0,0]

for ii in range(len(current_state)):
    for jj in range(len(transition_matrix)):
        new_state[ii] += current_state[jj]*transition_matrix[jj][ii]

print(new_state)
####
# Lines 8-15 were copied and pasted,
# then line 20 was changed
####
current_state = new_state
new_state = [0,0]

for ii in range(len(current_state)):
    for jj in range(len(transition_matrix)):
        new_state[ii] += round(current_state[jj]*transition_matrix[jj][ii],2)

print(new_state)
