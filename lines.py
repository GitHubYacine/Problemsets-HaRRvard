import sys

lines_in_code = 0

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 2:
    if sys.argv[1].endswith(".py"):
        try: 
            with open(sys.argv[1]) as file:
                for line in file:
                    if line.startswith("#") or line == "\n":
                        continue
                    else:
                        lines_in_code += 1
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")

print(lines_in_code)