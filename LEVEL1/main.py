def print_asteroids(width, height):
    print('#'*(width+2))
    
    for i in range(height):
        print('#' + ':'*(width) + '#')
    print('#'*(width+2))
    print()
#print_asteroids(10, 4)



with open("Files/level1_1_small.in", "r") as f:
    data1 = [line.strip().split() for line in f if line.strip()]
    data2 = data1[1:]

print(data2)

for values in data2:
    print_asteroids(int(values[0]), int(values[1]))