months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August", 
    "September", "October", "November", "December"
]

def main():
    while True:
        date = user_input()
        converted_date = date_converter(date)
        if converted_date != "Invalid Date":
            print(converted_date)
            break
        else:
            print("Invalid date, please try again")
        
def user_input():
    while True:
        try:
            user_input = input("Date: ")
            if "/" in user_input:
                return user_input.split("/")
            elif "," in user_input:
                user_input = user_input.replace(",", "")
                return user_input.split()
            else:
                continue
        except:
            pass
        
def date_converter(checked_date):
    month, day, year = checked_date
    try:
        month = int(month)
    except ValueError:
        month = months.index(month) + 1
    try: 
        day = int(day)
        year = int(year)
    except ValueError:
        return "Invalid date"
    if 1 <= month <= 12 and 1 <= day <= 31 and 0 < year:
        return f"{year}-{month:02}-{day:02}"
    else:
        return "Invalid Date"
        
main()

