l = []

def makefile(lines, filename):
    with open(f"Out/{filename}.out", "a") as f:
        #f.write(str() + "\n")
        for l in lines:
            f.write(l+ "\n")