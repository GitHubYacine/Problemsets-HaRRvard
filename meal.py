def main():
    user_input = input("What time is it? ").lower().strip()
    noon_check = noon_checker(user_input)
    converted_time = convert(user_input, noon_check)
    can_we_eat = (time_to_eat(converted_time))
    print(can_we_eat)

def noon_checker(noon):
    if 'am' in noon or 'a.m' in noon:
        return "am"
    elif 'pm' in noon or 'p.m' in noon:
        return "pm"
    else:
        return "24h"
    
def convert(time, is_noon):
    parts = time.split(":")
    hours = float(parts[0][:2])
    minutes = float(parts[1][:2]) / 60
    if is_noon == "pm" and hours < 12:
        hours += 12
    user_time = hours + minutes
    return user_time

def time_to_eat(time_check):
    if time_check >= 7 and time_check <= 8:
        return("breakfast time")
    elif time_check >= 12 and time_check <= 13:
        return("lunch time")
    elif time_check >= 18 and time_check <= 19:
        return("dinner time")
    else:
        return("not time for food")
    
main()