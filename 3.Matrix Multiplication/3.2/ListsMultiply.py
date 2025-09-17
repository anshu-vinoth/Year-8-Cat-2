state2 = [0.5,0.5]

matrix2 = [
     [0.1,0.9],
     [0.2,0.8]
]

current2 = [0,0]

for ii in range(len(state2)):
    for jj in range(len(matrix2)):
        current2[ii] += state2[jj]*matrix2[jj][ii]
        
print(current2)