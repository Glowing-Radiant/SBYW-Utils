import random

def get_valid_input(prompt, input_type, min_val=None, max_val=None):
    while True:
        try:
            value = input_type(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be greater than or equal to {min_val}.")
            elif max_val is not None and value > max_val:
                print(f"Value must be less than or equal to {max_val}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please try again.")

def generate_object(obj_type, x, y, z, length, breadth, height):
    if obj_type == "staircase":
        return f"staircase {x} {x + length} {y} {y + breadth} 0 {z} {height} wallgeneric\n"
    # Add more object types here

def check_collision(obj, objects):
    for existing_obj in objects:
        if (
            obj[0] >= existing_obj[0]
            and obj[0] < existing_obj[2]
            and obj[1] >= existing_obj[1]
            and obj[1] < existing_obj[3]
        ) or (
            obj[2] > existing_obj[0]
            and obj[2] <= existing_obj[2]
            and obj[3] > existing_obj[1]
            and obj[3] <= existing_obj[3]
        ):
            return True
    return False

def generate_objects(map_file, num_objects, obj_type, min_height, max_height, min_length, max_length, min_breadth, max_breadth, x_min, x_max, y_min, y_max):
    objects = []
    with open(map_file, "a") as f:
        for _ in range(num_objects):
            while True:
                x = random.randint(x_min, x_max - max_length)
                y = random.randint(y_min, y_max - max_breadth)
                z = random.randint(min_height, max_height)
                length = random.randint(min_length, max_length)
                breadth = random.randint(min_breadth, max_breadth)
                obj = (x, y, x + length, y + breadth)
                if not check_collision(obj, objects):
                    obj_line = generate_object(obj_type, x, y, z, length, breadth, z)
                    f.write(obj_line)
                    objects.append(obj)
                    break

def main():
    dmode = input("Do you want to create a 2d map or 3d? ").lower()
    max_x = get_valid_input("Enter the length of the map: ", int, min_val=1)
    max_y = get_valid_input("Enter the breadth of the map: ", int, min_val=1)
    default_platform = input("Enter the platform name you want the map to be filled with: ")

    with open("map.txt", "w") as f:
        if dmode == "3d":
            f.write("dmode 3d\n")
        f.write(f"maxx {max_x}\n")
        f.write(f"maxy {max_y}\n")
        f.write(f"platform 0 {max_x} 0 {max_y} 0 {default_platform}\n")

    num_objects = get_valid_input("How many objects do you want to generate? ", int, min_val=1)
    obj_type = input("Name the object type you want to generate: ").lower()
    min_height = get_valid_input("Enter the minimum height of the object: ", int, min_val=0)
    max_height = get_valid_input("Enter the maximum height of the object: ", int, min_val=min_height)
    min_length = get_valid_input("Enter the minimum length of the object: ", int, min_val=1)
    max_length = get_valid_input("Enter the maximum length of the object: ", int, min_val=min_length)
    min_breadth = get_valid_input("Enter the minimum breadth of the object: ", int, min_val=1)
    max_breadth = get_valid_input("Enter the maximum breadth of the object: ", int, min_val=min_breadth)
    specified_x_min = get_valid_input("Enter the minimum x coordinate of the specified area: ", int, min_val=0, max_val=max_x - max_length)
    specified_x_max = get_valid_input("Enter the maximum x coordinate of the specified area: ", int, min_val=specified_x_min + max_length, max_val=max_x)
    specified_y_min = get_valid_input("Enter the minimum y coordinate of the specified area: ", int, min_val=0, max_val=max_y - max_breadth)
    specified_y_max = get_valid_input("Enter the maximum y coordinate of the specified area: ", int, min_val=specified_y_min + max_breadth, max_val=max_y)

    generate_objects("map.txt", num_objects, obj_type, min_height, max_height, min_length, max_length, min_breadth, max_breadth, specified_x_min, specified_x_max, specified_y_min, specified_y_max)
    print(f"Generated {num_objects} {obj_type} objects in the map.txt file in your working directory.")

if __name__ == "__main__":
    main()
    