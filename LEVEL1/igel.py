def print_asteroids(width, height):
    print('#'*width)
    
    for i in range(height):
        print('#' + ':'*(width-2) + '#')
        
print_asteroids(10, 4)
