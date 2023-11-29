import re

def main():
    url = input("What's the YouTube video ID or embed URL? ")
    youtube_url = convert_to_youtube_url(url)
    if youtube_url:
        print("Standard YouTube URL:", youtube_url)
    else:
        print("Invalid YouTube video ID or embed URL format.")

def parse(url):
    pattern = r"^(https?://)?(www\.)?youtube\.com/embed/(.+)$"
    match = re.search(pattern, url)
    if match:
        return match.group(3)
    else:
        
        return url

def convert_to_youtube_url(url_or_id):
    video_id = parse(url_or_id)
    if video_id:
        return f"https://www.youtube.com/watch?v={video_id}"
    else:
        return None

if __name__ == "__main__":
    main()  