# 1.1 

def count_letters (path):
    counts = {}  # dictionary to store counts
    
    # open file and read line by line
    with open(path, "r") as f:
        for line in f:
            letter = line.strip()   # remove spaces/newlines
            # if letter already counted, add 1
            if letter in counts:
                counts[letter] += 1
            # if not seen before, start at 1
            else:
                counts[letter] = 1
    
    # print results like D:2, E:4 ...
    output = []
    for k, v in counts.items():
        output.append(f"{k}:{v}")
    print(", ".join(output))

# run the program
count_letters(".//1.DataStructures//1.1//data_structure_data.txt")
