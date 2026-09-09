input_filename = "level1_2_large.in"
content = open(input_filename, "r").read().strip()
num_astroids = int(content.splitlines()[0])
lines = content.splitlines()[1:]

def generate_print_astroid(x,y,infill = ":" , surrounding = "#"):
    x += 2
    y += 2
    multiline_string = """"""
    for i in range(y):
        if i == 0 or i == y-1:
            multiline_string += surrounding * x + "\n"
        
            print(surrounding * x)
        else:
            multiline_string += surrounding + infill * (x-2) + surrounding + "\n"
            print(surrounding + infill * (x-2) + surrounding)
    
    return multiline_string.strip()

output_string = """"""
for line in lines:
    x,y = map(int, line.split())

    output_string += generate_print_astroid(x,y)
    output_string += "\n\n"
    print()
with open(input_filename[:-3] + ".out", "w") as f:
    f.write(output_string)