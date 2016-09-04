import os
import re

def getExtension(filename):
    parts = os.path.splitext(filename)
    extension = parts[1].lower()
    return extension

def getSeasonAndEp(filename):
    pattern = r'[sS]\d{2}[eE]\d{2}'
    return re.findall(pattern, filename)[0]

def isPartOfSeries(filename):
    pattern = r'[sS]\d{2}[eE]\d{2}'
    if re.search(pattern, filename):
        return True
    return False

# return the filename string without the extension
def stripOfExtension(filename):
    extension = getExtension(filename)
    return filename[:-len(extension)]

video_ext = ('.mkv', '.avi', '.mp4', '.wmv', '.mov', '.webm')
subtitle_ext = ('.srt', '.sub', '.sbv')

series_files = [f for f in os.listdir('.') if f.endswith(video_ext) and isPartOfSeries(f)]
subtitle_files = [f for f in os.listdir('.') if f.endswith(subtitle_ext)]

# Using a simple O(N^2) search because there aren't that many files
for vid_file in series_files:
    vid_tag = getSeasonAndEp(vid_file)

    for sub_file in subtitle_files:
        sub_tag = getSeasonAndEp(sub_file)
        
        if vid_tag.lower() == sub_tag.lower():
            head = stripOfExtension(vid_file)
            os.rename(sub_file, head + getExtension(sub_file))
