l = []

def makefile(lines):
    with open("Out/level1_1_small.out", "a") as f:
        #f.write(str() + "\n")
        for l in lines:
            f.write(l+ "\n")