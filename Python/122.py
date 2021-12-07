import random

input = [1, 2, 3, 4, 5]

output = []

while(len(input)>0):
    index = random.randint(0, len(input)-1)
    output.append(input[index])
    del input[index]

print(output)