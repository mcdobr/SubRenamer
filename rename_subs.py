import os
import re

def get_extension(filename):
    parts = os.path.splitext(filename)
    extension = parts[1].lower()
    return extension

def get_season_and_ep(filename):
    pattern = r'[sS]\d{2}[eE]\d{2}'
    return re.findall(pattern, filename)[0]

def is_part_of_series(filename):
    pattern = r'[sS]\d{2}[eE]\d{2}'
    if re.search(pattern, filename):
        return True
    return False

# return the filename string without the extension
def strip_extension(filename):
    extension = getExtension(filename)
    return filename[:-len(extension)]

video_ext 	= ('.mkv', '.avi', '.mp4', '.wmv', '.mov', '.webm')
subtitle_ext    = ('.srt', '.sub', '.sbv')

series_files 	= [f for f in os.listdir('.') if f.endswith(video_ext) and is_part_of_series(f)]
subtitle_files 	= [f for f in os.listdir('.') if f.endswith(subtitle_ext)]

# Using a simple O(N^2) search because there aren't that many files
for vid_file in series_files:
    vid_tag = get_season_and_ep(vid_file)

    for sub_file in subtitle_files:
        sub_tag = get_season_and_ep(sub_file)
        
        if vid_tag.lower() == sub_tag.lower():
            head = strip_extension(vid_file)
            os.rename(sub_file, head + get_extension(sub_file))
