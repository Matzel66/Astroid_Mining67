def print_asteroids(width, height):
    print('#'*width)
    
    for i in range(height):
        print('#' + ':'*(width-2) + '#')
        
print_asteroids(10, 4)



with open("Files/level1_0_example.in", "r") as f:
    data1 = [line.strip().split() for line in f if line.strip()]
    data2 = data1[1:]

print(data2)