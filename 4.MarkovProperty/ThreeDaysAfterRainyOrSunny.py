
# There is a 50% chance that the town is rainy or sunny on the initial day
initial_state = [0.5,0.5]

transition_matrix = [
     [0.2,0.8],
     [0.4,0.6]
]
current_state = initial_state
new_state = [0,0]

for ii in range(len(current_state)):
    for jj in range(len(transition_matrix)):
        new_state[ii] += round(current_state[jj]*transition_matrix[jj][ii],3)

print(new_state)
####
# Lines 9-16 were copied and pasted,
# then line 21 was changed
####
current_state = new_state
new_state = [0,0]

for ii in range(len(current_state)):
    for jj in range(len(transition_matrix)):
        new_state[ii] += round(current_state[jj]*transition_matrix[jj][ii],3)

print(new_state)

####
# We multiply by our transition matrix 3 times in total, 1 for each day.
####
current_state = new_state
new_state = [0,0]

for ii in range(len(current_state)):
    for jj in range(len(transition_matrix)):
        new_state[ii] += round(current_state[jj]*transition_matrix[jj][ii],3)

# This output tells us that there is a 33.2% Chance it will be Sunny
# And a 66.8% Chance it will be Rainy.
print(new_state)
