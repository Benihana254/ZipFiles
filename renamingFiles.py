# renaming files with string slicing
import os
prefix_to_remove = 'y2mate.com - '
song_folder = r'C:\Users\gh\Music'
for filename in os.listdir(song_folder):
    if filename.startswith(prefix_to_remove):
        old_path = os.path.join(song_folder, filename)
        #string slicing filename[13:]
        new_path = os.path.join(song_folder, filename[len(prefix_to_remove):])
        os.rename(old_path, new_path)
        print('done')