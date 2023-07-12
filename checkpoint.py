#generate random  checkpoints on a 2d map.
import random
amount=int(input("how many checkpoints you want to generate"))
minx=int(input("enter the minimum specified x you want the checkpoints to spawn in."))
maxx=int(input("enter the maximum amount of x you want the checkpoints to spawn in"))
miny=int(input("enter the minimum y for the same"))
maxy=int(input("enter the maximum y for the same"))
def run():
  f=open("map.txt", "a")
  random_x=random.randint(minx, maxx)
  random_y=random.randint(miny, maxy)
  content=f"checkpoint {random_x} {random_y} \n"
  f.write(content)
  f.close()
for x in range(0, amount):
  run()
print(f"{amount} checkpoints generated and written to map.txt in your working directory")
