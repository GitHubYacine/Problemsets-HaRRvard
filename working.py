import re
def main():
    print(convert(input("Hours: ")))
    
def convert(time):
    if match := re.search(r"^([0-9]{1,2}):?([0-9]{1,2})?(?: ?)([AM|PM]{2})?(?: ?)[to].(?: ?)([0-9]{1,2}):?([0-9]{1,2})?(?: ?)([PM|AM]{2})?$", time, re.IGNORECASE):
        start_hours, start_minutes, start_ampm, end_hours, end_minutes, end_ampm = match.groups()
        
        start_hours = int(start_hours)
        start_minutes = int(start_minutes) if start_minutes else 0
        start_ampm = start_ampm.upper() if start_ampm else None
        
        end_hours = int(end_hours)
        end_minutes = int(end_minutes) if end_minutes else 0
        end_ampm = end_ampm.upper() if end_ampm else None
    else:
        raise ValueError("Invalid Time dawg")    
    
    if not validate_time(start_hours, start_minutes, start_ampm) or not validate_time(end_hours, end_minutes, end_ampm):
        raise ValueError("Invalid Time")
    
    start_24 = convert_to_24(start_hours, start_minutes, start_ampm)
    end_24 = convert_to_24(end_hours, end_minutes, end_ampm)

    return f"{start_24} to {end_24}"
    
def validate_time(hours, minutes, ampm):
    if ampm in ["AM", "PM"] and (hours < 0 or hours > 12):
        return False
    if not ampm in ["AM", "PM"] and (hours < 0 or hours > 23):
        return False
    if minutes < 0 or minutes > 59:
        return False
    return True
    
def convert_to_24(hours, minutes, ampm):
    if ampm == "PM" and hours != 12:
        hours += 12
    elif ampm == "AM" and hours == 12:
        hours = 0
    return f"{hours:02d}:{minutes:02d}"
        
if __name__ == "__main__":
    main()