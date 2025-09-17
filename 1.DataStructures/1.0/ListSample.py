# Declaring an empty list

Fruit = []

#Assigning values to the list
# Note: "apples" is the key, and 10 is the value that goes with that key.
Fruit.append("apples")
Fruit.append("pears")

# ["apples","pears"]
print(Fruit)

# Overwriting the value of a key
Fruit[0] = "orange"
# ["orange","pears"]
print(Fruit)

# Declaring a list with some values
# A list of sports
Sports = ["soccer","badminton","ballet"]
# A list of counts that match the sports based on index.
Sports_Count = [10,5,10]
#["soccer","badminton","ballet"]
print(Sports)
#[10,5,10]
print(Sports_Count)

for sport in Sports:
    print(sport)

for ii in range(len(Sports)):
    print(Sports[ii])

for ii in range(len(Sports_Count)):
    value = Sports_Count[ii]
    if value % 2 == 0:
        print(value,"is even!")

Matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print(Matrix)

for ii in range(len(Matrix)):
    for jj in range(len(Matrix[0])):
        print(Matrix[ii][jj])