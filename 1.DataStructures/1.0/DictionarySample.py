# Declaring an empty dictionary

Fruit = {}

#Assigning values to the dictionary
# Note: "apples" is the key, and 10 is the value that goes with that key.
Fruit["apples"] = 10

# {'apples': 10}
print(Fruit)

# Overwriting the value of a key
Fruit["apples"] = "hello world"
#{'apples': 'hello world'}
print(Fruit)

# Declaring a dictionary with keys and values
# Note: ' "soccer":10 ' together are a Key Value pair.
Sports = {"soccer":10,"badminton":5,"ballet":4}

#{'soccer': 10, 'badminton': 5, 'ballet': 4}
print(Sports)

# Looping through the key,value pairs in a dictionary
for key,value in Sports.items():
    # soccer 10
    # badminton 5
    # ballet 4
    print(key,value)

    # This is how you check if a number is even
    if value % 2 == 0:
        print(value,"is even!")