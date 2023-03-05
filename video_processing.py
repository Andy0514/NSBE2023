from moviepy.editor import *
from os import listdir
from os.path import isfile, join, splitext

#  Setup - get the list of all available words in the dictionary
video_dict = dict()
video_dir = "videos"
for f in listdir(video_dir):
    if isfile(join(video_dir, f)):
        video_dict.add(splitext(f)[0], join(video_dir, f))


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

    final_clip.write_videofile(tempfile)
    return tempfile



