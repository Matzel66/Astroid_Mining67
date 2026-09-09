input_filename = "level2_2_large.in"
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

def drill_adtroid(astroid_array, drill_at = "S" , drill_with = "X"):
    drill = False
    for i in range(len(astroid_array)):
        for j in range(len(astroid_array[i])):
            if astroid_array[i][j] == drill_at:
                Xposition = j
                Yposition = i
                drill = True
                continue
            if drill:
                if j == Xposition and i >= Yposition:
                    
                    if i == len(astroid_array) - 1:
                        continue
                    else:
                        astroid_array[i] = astroid_array[i][:j] + drill_with + astroid_array[i][j+1:]
    return astroid_array

print(astroids)
drilled_string = ""
for astroid in astroids:
    drilled_string += "\n".join(drill_adtroid(astroid))
    drilled_string += "\n\n"

with open(input_filename[:-3] + ".out", "w") as f:
    f.write(drilled_string.strip())
