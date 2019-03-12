cubemain = []
for i in range(6):
  cubemain.append([i,i,i,i])

print(str(cubemain))

front = cubemain[0]
back = cubemain[1]
left = cubemain[2]
right = cubemain[3]
up = cubemain[4]
bottom = cubemain[5]

f0 = front[0]
f1 = front[1]
f2 = front[2]
f3 = front[3]
b0 = back[0]
b1 = back[1]
b2 = back[2]
b3 = back[3]
l0 = left[0]
l2 = left[1]
l2 = left[2]
l3 = left[3]
r0 = right[0]
r1 = right[1]
r2 = right[2]
r3 = right[3]
u0 = up[0]
u1 = up[1]
u2 = up[2]
u3 = up[3]
bo0 = bottom[0]
bo1 = bottom[1]
bo2 = bottom[2]
bo3 = bottom[3]

def front(cubemain):
  cube = cubemain #0
  front = cube[0]
  back = cube[1]
  left = cube[2]
  right = cube[3]
  up = cube[4]
  bottom = cube[5]

  f0 = front[0]
  f1 = front[1]
  f2 = front[2]
  f3 = front[3]
  b0 = back[0]
  b1 = back[1]
  b2 = back[2]
  b3 = back[3]
  l0 = left[0]
  l2 = left[1]
  l2 = left[2]
  l3 = left[3]
  r0 = right[0]
  r1 = right[1]
  r2 = right[2]
  r3 = right[3]
  u0 = up[0]
  u1 = up[1]
  u2 = up[2]
  u3 = up[3]
  bo0 = bottom[0]
  bo1 = bottom[1]
  bo2 = bottom[2]
  bo3 = bottom[3]
  u3, bo1 = bo1, u3
  u2, bo0 = bo0, u2
  r0, l2 = l2, r0
  r3, l1 = l1, r3
  f0, f2 = f2, f0
  f1, f3 = f3, f1

def back(cubemain):
  cube = cubemain #1
  front = cube[0]
  back = cube[1]
  left = cube[2]
  right = cube[3]
  up = cube[4]
  bottom = cube[5]

  f0 = front[0]
  f1 = front[1]
  f2 = front[2]
  f3 = front[3]
  b0 = back[0]
  b1 = back[1]
  b2 = back[2]
  b3 = back[3]
  l0 = left[0]
  l2 = left[1]
  l2 = left[2]
  l3 = left[3]
  r0 = right[0]
  r1 = right[1]
  r2 = right[2]
  r3 = right[3]
  u0 = up[0]
  u1 = up[1]
  u2 = up[2]
  u3 = up[3]
  bo0 = bottom[0]
  bo1 = bottom[1]
  bo2 = bottom[2]
  bo3 = bottom[3]
  u0, bo2 = bo2, u0
  u1, bo3 = bo3, u1
  r1, l3 = l3, r1
  r2, l0 = l0, r2
  b0, b3 = b3, b0
  b1, b2 = b2, b1

def left(cubemain):
  cube = cubemain #2
  front = cube[0]
  back = cube[1]
  left = cube[2]
  right = cube[3]
  up = cube[4]
  bottom = cube[5]

  f0 = front[0]
  f1 = front[1]
  f2 = front[2]
  f3 = front[3]
  b0 = back[0]
  b1 = back[1]
  b2 = back[2]
  b3 = back[3]
  l0 = left[0]
  l2 = left[1]
  l2 = left[2]
  l3 = left[3]
  r0 = right[0]
  r1 = right[1]
  r2 = right[2]
  r3 = right[3]
  u0 = up[0]
  u1 = up[1]
  u2 = up[2]
  u3 = up[3]
  bo0 = bottom[0]
  bo1 = bottom[1]
  bo2 = bottom[2]
  bo3 = bottom[3]
  u0, bo0 = bo0, u0
  u3, bo3 = bo3, u3
  f0, b0 = b0, f0
  f3, b3 = b3, f3
  l0, l2 = l2, l0
  l1, l3 = l3, l1

def right(cubemain):
  cube = cubemain #3
  front = cube[0]
  back = cube[1]
  left = cube[2]
  right = cube[3]
  up = cube[4]
  bottom = cube[5]

  f0 = front[0]
  f1 = front[1]
  f2 = front[2]
  f3 = front[3]
  b0 = back[0]
  b1 = back[1]
  b2 = back[2]
  b3 = back[3]
  l0 = left[0]
  l2 = left[1]
  l2 = left[2]
  l3 = left[3]
  r0 = right[0]
  r1 = right[1]
  r2 = right[2]
  r3 = right[3]
  u0 = up[0]
  u1 = up[1]
  u2 = up[2]
  u3 = up[3]
  bo0 = bottom[0]
  bo1 = bottom[1]
  bo2 = bottom[2]
  bo3 = bottom[3]
  u1, bo1 = bo1, u1
  u2, bo2 = bo2, u2
  f1, b1 = b1, f1
  f2, b2 = b2, f2
  r0, r2 = r2, r0
  r1, r3 = r3, r1

def up(cubemain):
  cube = cubemain #4
  front = cube[0]
  back = cube[1]
  left = cube[2]
  right = cube[3]
  up = cube[4]
  bottom = cube[5]

  f0 = front[0]
  f1 = front[1]
  f2 = front[2]
  f3 = front[3]
  b0 = back[0]
  b1 = back[1]
  b2 = back[2]
  b3 = back[3]
  l0 = left[0]
  l2 = left[1]
  l2 = left[2]
  l3 = left[3]
  r0 = right[0]
  r1 = right[1]
  r2 = right[2]
  r3 = right[3]
  u0 = up[0]
  u1 = up[1]
  u2 = up[2]
  u3 = up[3]
  bo0 = bottom[0]
  bo1 = bottom[1]
  bo2 = bottom[2]
  bo3 = bottom[3]
  f0, b2 = b2, f0
  f1, b3 = b3, f1
  r0, l0 = l0, r0
  r1, l1 = l1, r1
  u0, u2 = u2, u0
  u1, u3 = u3, u1

def bottom(cubemain):
  cube = cubemain #5
  front = cube[0]
  back = cube[1]
  left = cube[2]
  right = cube[3]
  up = cube[4]
  bottom = cube[5]

  f0 = front[0]
  f1 = front[1]
  f2 = front[2]
  f3 = front[3]
  b0 = back[0]
  b1 = back[1]
  b2 = back[2]
  b3 = back[3]
  l0 = left[0]
  l2 = left[1]
  l2 = left[2]
  l3 = left[3]
  r0 = right[0]
  r1 = right[1]
  r2 = right[2]
  r3 = right[3]
  u0 = up[0]
  u1 = up[1]
  u2 = up[2]
  u3 = up[3]
  bo0 = bottom[0]
  bo1 = bottom[1]
  bo2 = bottom[2]
  bo3 = bottom[3]
  f3, b1 = b1, f3
  f2, b0 = b0, f2
  r3, l3 = l3, r3
  r2, l2 = l2, r2
  bo0, bo2 = bo2, bo0
  bo1, bo3 = bo3, bo1
