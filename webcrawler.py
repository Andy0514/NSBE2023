import requests
import wget
from bs4 import BeautifulSoup

count = 0
videos = []

for i in range(1, 10000):
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
            videos.append("https://www.handspeak.com" + video_url)
            break

    count += 1
    if (count * 100) / 10950 in {10, 20, 30, 40, 50, 60, 70, 80, 90}:
        print(str((count * 100) / 10950) + "% finished")

print("Found " + str(len(videos)) + " videos")

def getWord(videos):
    w = []
    for i in videos:
        endP = 0
        startP = 0
        r = i[::-1]
        for s in range(len(r)):
            if r[s] == ".":
                endP = s + 1
                if r[s + 1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                    endP = s + 2
            if r[s] == "/":
                startP = s
                break
        print(startP, endP)
        w.append(r[endP:startP][::-1])
    return w

words = getWord(videos)

def getFileName(words):
    w = []
    for i in words:
        f = i + ".mp4"
        w.append(f)
    return w

fileNames = getFileName(words)
print(fileNames)

print(words)

def downloadVideos(videos, fileNames):
    for i in range(len(videos)):
        try:
            response = wget.download(videos[i], fileNames[i])
        except:
            print(videos[i], fileNames[i], i)

downloadVideos(videos, fileNames)
