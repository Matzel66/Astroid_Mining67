def print_asteroids(width, height):
    lines = []
    lines.appned('#'*(width+2))
    
    for i in range(height):
        lines.append('#' + ':'*(width) + '#')
    lines.append('#'*(width+2))

print_asteroids(10, 4)
