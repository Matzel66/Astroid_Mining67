input_filename = "level3_1_small.in"
content = open(input_filename, "r").read().strip()
num_astroids = int(content.splitlines()[0])
lines = content.splitlines()[1:]
#print(lines)

def remove_first_n_elments(input_array, n):
    return input_array[n:]

def generate_astroid_arrays(input_array):
    all_arr = []
    current_arr = []
    for line in input_array:
        if line == '':
            if current_arr: 
                all_arr.append(remove_first_n_elments(current_arr, 1))
            current_arr = []
        else:
            current_arr.append(line)
    
    
    if current_arr:
        all_arr.append(remove_first_n_elments(current_arr, 1))
    
    return all_arr

astroids = generate_astroid_arrays(lines)

def drill_asteroid(asteroid_array, drill_at="S", drill_with="X"):
    
    asteroid_array = [list(row) for row in asteroid_array]
    
    drill = False
    sizeX = len(asteroid_array[0]) - 2
    sizeY = len(asteroid_array) - 2
    
    for i in range(len(asteroid_array)):
        for j in range(len(asteroid_array[i])):
            if asteroid_array[i][j] == drill_at:
                Xposition = j
                Yposition = i
                drill = True
                

                
                if i + 1 < len(asteroid_array):
                    print(asteroid_array[i + 1][j])
                    asteroid_array[i + 1][j] = drill_with
                continue
            
            if sizeX == 3 and drill:
                if i == 0 or i == len(asteroid_array) - 1:
                    continue
                asteroid_array[i][2] = drill_with
            if sizeY == 3 and drill:
                if j == 0 or j == len(asteroid_array[i]) - 1:
                    continue
                asteroid_array[2][j] = drill_with
    
    
    return ["".join(row) for row in asteroid_array]


print(astroids)
drilled_string = ""
for astroid in astroids:
    drilled_string += "\n".join(drill_asteroid(astroid))
    drilled_string += "\n\n"

with open(input_filename[:-3] + ".out", "w") as f:
    f.write(drilled_string)
