import sys, csv
from tabulate import tabulate

data_list = []

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 2:
    if sys.argv[1].endswith(".csv"):
        try: 
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for row in reader:
                    data_list.append(row)
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")

print(tabulate(data_list, tablefmt="grid"))