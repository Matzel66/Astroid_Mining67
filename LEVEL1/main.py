from igel import *
from Parser import *
from deparser import *

file_name = "Files/level1_0_example.in"

data2 = parse(file_name)
print(data2)

for values in data2:
    makefile(print_asteroids(int(values[0]), int(values[1])), file_name.split('/')[1].split('.')[0])