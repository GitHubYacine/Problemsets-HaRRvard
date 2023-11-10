subs = []

with open("subscribers.csv") as file:
    for line in file:
        name, sub_length = line.rstrip().split(",")
        sub = {"name": name, "sub_length": sub_length}
        subs.append(sub)

def get_name(sub):
    return sub["name"]

def get_sub_length(sub):
    return sub["sub_length"]
   
for sub in sorted(subs, key=lambda sub: sub["name"]):    
    print(f"{sub['name']} has been subscribed for {sub['sub_length']}")