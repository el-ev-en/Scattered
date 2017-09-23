# I need to make the output prettier
# Make it possible to spill the water multiple times


import random
end = 0


# The big cycle to run program anew every time
while end != 1:

  length = int(input("how long the line should be?"))
  line = []
  for a in range(length): #populating the line
    line.append("X")

  print(line)

  b = int(input("where to spill the water?")) #choosing the coordinates

  c = int(input("How much water to spill (1 minimum)?"))

  #filling the starting space with water

  line[b] = "~"
  c = c - 1
  e = 0

  # while there is at least 2 items of water, we can spill it symetricaly
  while c > 2:
    e += 1
    line[b-e] = "~"
    line[b+e] = "~"
    c -= 2

# if there is some water left, we should assign the space for it at random

  if c == 1:
    if random.randrange(2) == 1:
      line[b + e + 1] = "~"
    else:
      line[b - e - 1] = "~"


  print(line)

#the way to stop the iterations of the program
  end = int(input("press 0 to continue, write 1 to stop the program"))
