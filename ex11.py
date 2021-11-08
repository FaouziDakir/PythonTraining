directions = ['north', 'east', 'south', 'west']

coordinates = {"x" : 7, "y" : 3}

instructions = "RAALAL"

def execute(instr):
    actualDirection = 'north'
    for char in instr :
        if char == 'A':
            if actualDirection == 'north':
                coordinates['y'] = coordinates['y'] + 1
            elif actualDirection == 'south':
                coordinates['y'] = coordinates['y'] - 1
            elif actualDirection == 'east':
                coordinates['x'] = coordinates['x'] + 1
            elif actualDirection == 'west':
                coordinates['x'] = coordinates['x'] - 1
        elif char == 'R':
            index = directions.index(actualDirection)
            if(index == 3):
                index = 0
                actualDirection = directions[index]
            else:
                actualDirection = directions[index + 1]
        elif char == 'L':
            index = directions.index(actualDirection)
            if(index == 0):
                index = 3
                actualDirection = directions[index]
            else:
                actualDirection = directions[index - 1]        
        else :
            return 'Your instructions contains a forbidden character (only ARL).'
    return actualDirection

execute(instructions)

print(coordinates)
actualDirection = execute(instructions)
print(actualDirection)