import os

# Change name of the playlist before .m3u8
playlist_name = "Day6.m3u8"
playlist_path = "C://Users//longn//Music//Playlists//" + playlist_name

# This is the music folder path
folder_path = "C://Users//longn//Music//Day6"

# Reading file name in the folder
folder_list = os.listdir(folder_path)

# Writing playlist file
with open(playlist_path, "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    f.write("#" + playlist_name + "\n")
    folder_path_string = "\\".join(folder_path.split("//"))
    for file_path in folder_list:
        temp = folder_path_string + "\\" + file_path + "\n"
        f.write(temp)
