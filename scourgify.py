import sys, csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) == 3:
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        try: 
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                with open(sys.argv[2], "w", newline="") as csvfile:
                    fieldnames = ["first_name", "last_name", "house"]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    for line in reader:
                        last_name, first_name = (line["name"].split(", "))
                        writer.writerow({"first_name": first_name, "last_name": last_name, "house": line["house"]})
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
    else:
        sys.exit("You did not enter any .csv files")