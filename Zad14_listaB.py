import math

def robot():
    print("Please choose direction to go and number of steps for your robot. To start, type 'GO!'")
    actual_pos = [0, 0]
    while True:
        my_input = input("")
        movement = my_input.split(" ")
        if "GO!" in my_input:
            break
        elif len(movement) <= 1:
            return ValueError("WRONG COMMAND!")
        elif "UP" in my_input:
            actual_pos = [actual_pos[0], actual_pos[1] + int(movement[1])]
        elif "DOWN" in my_input:
            actual_pos = [actual_pos[0], actual_pos[1] - int(movement[1])]
        elif "LEFT" in my_input:
            actual_pos = [actual_pos[0] - int(movement[1]) , actual_pos[1]]
        elif "RIGHT" in my_input:
            actual_pos = [actual_pos[0] + int(movement[1]) , actual_pos[1]]
        else:
            return ValueError("WRONG COMMAND!")

    distance = round(math.sqrt((math.pow((actual_pos[0]), 2)) + math.pow((actual_pos[1]), 2)))
    return distance

print(robot())






