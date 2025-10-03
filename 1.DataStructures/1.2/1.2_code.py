# 1.1 COUNT LETTERS -----------------------
def count_letters(filename):
    counts = {}  # dictionary for counts
    
    with open(filename, "r") as f:
        for line in f:
            letter = line.strip()  # remove spaces/newlines
            # add to dictionary
            counts[letter] = counts.get(letter, 0) + 1
    
    # print result
    output = []
    for k, v in counts.items():
        output.append(f"{k}:{v}")
    print("Letter Counts ->", ", ".join(output))   # print here


# 1.2 LETTER PROBABILITIES ----------------
def letter_probabilities(filename):
    counts = {}
    total = 0  # total number of letters
    
    with open(filename, "r") as f:
        for line in f:
            letter = line.strip()
            counts[letter] = counts.get(letter, 0) + 1
            total += 1
    
    # convert to probabilities
    output = []
    for k, v in counts.items():
        prob = v / total  # count ÷ total
        output.append(f"{k}:{prob:.2f}")
    print("Letter Probabilities ->", ", ".join(output))  # print here


# ==========================
# RUN THE FUNCTIONS
# ==========================
count_letters(".//1.DataStructures//1.1//data_structure_data.txt")
letter_probabilities(".//1.DataStructures//1.1//data_structure_data.txt")
