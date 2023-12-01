import re

def main():
    print(parse(input("What's the URL? ")))

def parse(url):
    if match := re.search(r'(?:https?://)?(?:www\.)?youtube\.com/embed/([^"]+)', url):
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    
    
if __name__ == "__main__":
    main()  