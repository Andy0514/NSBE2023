from moviepy.editor import *
from os import listdir
from os.path import isfile, join, splitext
import os
import cohere
import pickle
co = cohere.Client('yiOWD4KfXSiayGiim2MRmZRUvGsbdEFOY5QaCQ1Z') # This is your trial API key


#  Setup - get the list of all available words in the dictionary
video_dict = dict()
video_dir = "videos"
for f in listdir(video_dir):
    if isfile(join(video_dir, f)):
        if (f[-3:] == "mp4"):
            video_dict[splitext(f)[0]] = join(video_dir, f)

print("Found " + str(len(video_dict)) + " videos")

def text_to_video(input):
    tempfile = "concatenated.mp4"
    if os.path.exists(tempfile):
        os.remove(tempfile)

    words = input.split()
    finalClip = None
    for w in words:
        w = w.lower()
        if w in video_dict:
            # Directly found, use the video
            if finalClip == None:
                finalClip = VideoFileClip(video_dict[w])
            else:
                clip = VideoFileClip(video_dict[w])
                finalClip = concatenate_videoclips([finalClip, clip])
        else:
            # Word not directly matched in dictionary. Consider using an embedding?
            pass

    final_clip.write_videofile(tempfile)
    return tempfile



def compute_embeddings_one_time(words):
    embeddings = dict()
    i = 0
    temp = []
    for k in words.keys():
        if (i < 95):
            temp.append(k.split()[0])
            i += 1
        else:
            temp.append(k.split()[0])
            response = co.embed(texts=temp, model="small")
            for j in range(len(temp)):
                embeddings[temp[j]] = response.embeddings[j]
                if (temp[j] == "decide"):
                    print(response.embeddings[j])
                    print(len(response.embeddings))


            i = 0
            temp = []
    return embeddings

embed = compute_embeddings_one_time(video_dict)
with open('embeddings.pkl', 'wb') as fp:
    pickle.dump(embed, fp)
    print('Embeddings saved successfully to file')
