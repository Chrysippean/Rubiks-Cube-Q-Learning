cube = []
for i in range(6):
  cube.append([i,i,i,i])
  

def front: #0
  u3, bo1 = bo1, u3
  u2, bo0 = bo0, u2
  r0, l2 = l2, r0
  r3, l1 = l1, r3
  f0, f2 = f2, f0
  f1, f3 = f3, f1

def back: #1
  u0, bo2 = bo2, u0
  u1, bo3 = bo3, u1
  r1, l3 = l3, r1
  r2, l0 = l0, r2
  b0, b3 = b3, b0
  b1, b2 = b2, b1

def left: #2

  u0, bo0 = bo0, u0
  u3, bo3 = bo3, u3
  f0, b0 = b0, f0
  f3, b3 = b3, f3
  l0, l2 = l2, l0
  l1, l3 = l3, l1

def right: #3

  u1, bo1 = bo1, u1
  u2, bo2 = bo2, u2
  f1, b1 = b1, f1
  f2, b2 = b2, f2
  r0, r2 = r2, r0
  r1, r3 = r3, r1

def up: #4
  f0, b2 = b2, f0
  f1, b3 = b3, f1
  r0, l0 = l0, r0
  r1, l1 = l1, r1
  u0, u2 = u2, u0
  u1, u3 = u3, u1

def bottom: #5
  f3, b1 = b1, f3
  f2, b0 = b0, f2
  r3, l3 = l3, r3
  r2, l2 = l2, r2
  bo0, bo2 = bo2, bo0
  bo1, bo3 = bo3, bo1