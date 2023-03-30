import random

# Ask for user input
max_x = int(input("Enter the maximum length of the map: "))
platform_name = input("Enter the name of the default  platform of the map: ")
num_music_files = int(input("Enter the number of loop_music files to generate: "))
random_volume = input("Do you want to randomly generate the volume for each ambience line? (y/n): ").lower() == 'y'
random_pitch = input("Do you want to randomly generate the pitch for each ambience line? (y/n): ").lower() == 'y'
shuffle_music = input("Do you want to shuffle the music files? (y/n): ").lower() == 'y'

# Create a list of selected tiles
selected_tiles = list(range(1, num_music_files + 1))

# Shuffle the music files if requested
if shuffle_music:
    random.shuffle(selected_tiles)

# Create the map file
with open("map.txt", "w") as f:
    # Write the maxx line
    f.write(f"maxx {max_x}\n")

    # Write the platform line
    platform_line = f"platform 0 {max_x} 0 {platform_name}"
    f.write(platform_line + "\n")

    # Loop through the selected tiles and create an ambience line for each
    for i, x in enumerate(selected_tiles):
        volume = random.randint(-100, 0) if random_volume else 0
        pitch = random.randint(0, 200) if random_pitch else 100
        music_file_name = f"loop_music{x}.ogg"
        ambience_line = f"ambience {i+1} {i+1} 0 10 {music_file_name} {volume} {pitch}"
        zone_line = f"zone {i+1} {i+1} 0 10 {music_file_name.split('.')[0]}"
        # Write the line to the map file
        f.write(ambience_line + "\n")
        f.write(zone_line + "\n")


print(f"I have generated {num_music_files} and saved them into map.txt in your working directory.")
