PROBLEM_DESC=\
 '''
'''
# COLORS: B: black, W: white, R: red, Y: yellow, O: orange, P: pink 
COLORS={0: 'B', 1: 'W', 2: 'R', 3: 'Y', 4: 'O', 5: 'P'}

ACTIONS = ["Up", "Down", "Left", "Right", "Front", "Back"]
Opposite = ["Up", "Down"], ["Left", "Right"], ["Front", "Back"]

# R, L, Back, Up, Front, Back

# L -- FL <-> BL, UL <-> BotL, L - switch corners
# R -- FR <-> BR

# move % 2 == 0, opp = move + 1
# move % 2 == 1, opp = move - 1

# [0,1,2,3,4,5].remove(2).remove(3) => [0,1,4,5] -- 0 - 1, 4 - 5

# L - p1,p4
# R - p2,p3
# U - p1,p2
# B - p4,p3
# F - 

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

action = 'some action'

if action % 2 == 0:
  opp = action + 1
else:
  opp = action - 1

arr = [0,1,2,3,4,5].remove(action).remove(opp)



class State:
  def __init__(self, d):
    self.d = d

  def __eq__(self,s2):
    #############
    return True

  def __str__(self):
    #############

  def __hash__(self):
    return (self.__str__()).__hash__()

  def copy(self):
    # Performs an appropriately deep copy of a state,
    # for use by operators in creating new states.
    news = State({})
    ##############
    return news

  def can_move(self,From,To):
    try:
      ###############
    except (Exception) as e:
      print(e)

  def move(self,From,To):
    news = self.copy() # start with a deep copy.
    ###############
    return news # return new state

def make_goal_state():
  global GOAL_STATE, N_disks
  #GOAL_STATE = State({})
  #print("GOAL_STATE="+str(GOAL_STATE))

make_goal_state()

def goal_test(s):
  global GOAL_STATE
  return s==GOAL_STATE

def goal_message(s):
  return "#############"

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)

#</COMMON_CODE>

def CREATE_INITIAL_STATE():
  global INITIAL_STATE
  requestColors = input("Would you like to customize your Rubik's Cube? (y/n) ")
  if requestColors is 'y':
      getUserColors()
  return INITIAL_STATE
#</INITIAL_STATE>

def getUserColors():


#<OPERATORS>
OPERATORS = [Operator( )] 

# 26 cubies -- 8 corners, 12 edges, (not relevant: 6 centers)
# We need an array of 20 elements, encode position and orientation (3 for corner, 2 for edge)
  # (8! * 3**8 * 12! * 2**12) / 12 (up to isomorphism)

# 3 different moves for 6 different operators = BRANCHING FACTOR = 18
  # Twisting same face twice = redundant => 15
  # Twisting opposite faces  = redundant => asymptotic b-factor = 13.34


# https://ruwix.com/the-rubiks-cube/notation/



def goal_test(s):
  for face in range(5):
    color = cube[face][0]
    for tile in range(1,4):
      if cube[face][tile] != color:
        return false
  return true

def goal_message(s):
  return "Congratulations! The cube is solved!"


#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

