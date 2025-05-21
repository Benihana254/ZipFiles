import zipfile,os,shutil
#There exist a list of songs in the music folder
music_folder = r'C:\Users\gh\Music'
# This list all of them
songs = os.listdir(music_folder)
# creating a zipfile in the music folder
with zipfile.ZipFile(os.path.join(music_folder,'compressedSongs.zip'), 'w') as zip2f:
    for song in songs:
        full_song_path = os.path.join(music_folder,song)
        if os.path.isfile(full_song_path):
            zip2f.write(full_song_path, arcname=song)
print(os.path.abspath('compressedSongs.zip')) # not necessary
# This points to the exact path of the zip folder on the pc, not the cwd like in the above
zip_path = os.path.join(music_folder,'compressedSongs.zip')
# we assign the destination path
destination = r'C:\Users\gh\Desktop\FolderE'
os.makedirs(destination,exist_ok=True)
shutil.copy(zip_path,destination)
print("done")


# zip_path = os.path.abspath(r'C:\Users\gh\Music\compressedSongs.zip')
# shutil.copytree(zip_path, r'C:\Users\gh\Desktop\FolderB')