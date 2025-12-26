import os
import shutil

# Change name of the playlist before .m3u8
band_name = input("Enter you band/playlist name you want: ")
playlist_name = band_name + ".m3u8"
playlist_path = "C://Users//longn//Music//Playlists//" + playlist_name

# This is the music folder path
folder_path = input("Enter your music folder path you want to create a playlist: ")
folder_path = "//".join(folder_path.split("\\"))

# Reading file name in the folder
folder_list = os.listdir(folder_path)

# Create a folder with band name if there not exists
music_folder = "C://Users//longn//Music//" + band_name
try:
    os.mkdir(music_folder)
    print(f"=> Creating music folder {music_folder} successfully.")
except FileExistsError:
    print(f"=> Directory '{music_folder}' already exists.")
except Exception as e:
    print(f"=> An error occurred: {e}")
print()

# Copy files from the present folder to the music folder in C disk
if "C://Users//longn//Music//" not in folder_path:
    print("----Copying songs into the music folder----")
    count = 0
    music_folder_list = os.listdir(music_folder)
    for file_path in folder_list:
        if file_path not in music_folder_list:
            shutil.copy(os.path.join(folder_path, file_path), music_folder)
            print("Copy " + file_path + " -> Success")
            count += 1

    print(f"=> Copying {count} songs complete.")
        
print()

# Writing playlist file
if os.path.isfile(playlist_path):
    count = 0
    print("----Adding songs into the playlist----")
    contents = list()
    with open(playlist_path, "r", encoding="utf-8") as f:
        contents = f.readlines()

    with open(playlist_path, "a", encoding="utf-8") as f:
        for file_path in folder_list:
            temp = "\\".join(music_folder.split("//")) + "\\" + file_path + "\n"
            if temp not in contents:
                f.write(temp)
                print(f"Adding {temp[:-1]}")
                count+=1

    print(f"Adding {count} songs complete.")
else:
    count = 0
    print("----Creating playlist----")
    with open(playlist_path, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        f.write("#" + playlist_name + "\n")
        for file_path in folder_list:
            temp = "\\".join(music_folder.split("//")) + "\\" + file_path + "\n"
            f.write(temp)
            print(f"Adding {temp[:-1]}")
            count += 1

        print(f"=> Creating playlist {playlist_name} with {count} songs successfully.")
