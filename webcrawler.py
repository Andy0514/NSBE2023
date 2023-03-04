import requests
from bs4 import BeautifulSoup

count = 0
videos = []
for i in range(1, 10950):
    url = "https://www.handspeak.com/word/" + str(i) + "/"

    # Get URL Content
    r = requests.get(url)

    # Parse HTML Code
    soup = BeautifulSoup(r.content, 'html.parser')

    # List of all video tag
    video_tags = soup.findAll('video')
    for video_tag in video_tags:
        video_url = video_tag['src']
        if video_url != None:
            videos.append(video_url)

    count += 1
    if (count * 100) / 10950 in {10, 20, 30, 40, 50, 60, 70, 80, 90}:
        print(str((count * 100) / 10950) + "% finished")

print("Found " + str(len(videos)) + " videos")



