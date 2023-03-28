import random

# ask the user for the dimensions of the map
dmode = input("Do you want to create a 2d map or 3d? ")
max_x = int(input("Enter the length of the map: "))
max_y = int(input("Enter the breadth of the map: "))
default_platform = input("enter the platform name you want the map to be filled with.")
# write the dimensions to the file
with open("map.txt", "w") as f:
    if dmode == "3d":
        f.write("dmode 3d\n")
    f.write(f"maxx {max_x}\n")
    f.write(f"maxy {max_y}\n")
    f.write(f"platform 0 {max_x} 0 {max_y} 0 {default_platform}\n")

# ask the user for the number of objects to generate
num_objects = int(input("How many objects do you want to generate? "))

# ask the user for the type of object to generate
object_type = input("name the object tile you want to generate")

min_height = int(input("Enter the minimum height of the object: "))
max_height = int(input("Enter the maximum height of the object: "))
min_length = int(input("enter the maximum length of the object."))
max_length = int(input("enter the maximum length of the object"))
min_breadth = int(input("enter the maximum breadth of the object"))
max_breadth = int(input("enter the maximum breadth of the object"))
# ask the user for the specified area to generate the objects in
specified_x_min = int(input("Enter the minimum x coordinate of the specified area: "))
specified_x_max = int(input("Enter the maximum x coordinate of the specified area: "))
specified_y_min = int(input("Enter the minimum y coordinate of the specified area: "))
specified_y_max = int(input("Enter the maximum y coordinate of the specified area: "))

# generate the objects and write them to the file
with open("map.txt", "a") as f:
    for i in range(num_objects):
        # generate random coordinates within the specified area
        x = random.randint(specified_x_min, specified_x_max)
        y = random.randint(specified_y_min, specified_y_max)
        z = random.randint(min_height, max_height)
        length = random.randint(min_length, max_length)
        breadth = random.randint(min_breadth, max_breadth)
        l = x + length
        b = y + breadth
        f.write(f"staircase {x} {l} {y} {b} 0 {z} {object_type}\n")
