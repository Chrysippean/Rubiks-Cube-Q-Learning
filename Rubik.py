PROBLEM_DESC=\
 '''
'''
# COLORS: B: black, W: white, R: red, Y: yellow, O: orange, P: pink 
COLORS={0: 'B', 1: 'W', 2: 'R', 3: 'Y', 4: 'O', 5: 'P'}

ACTIONS = ["Up", "Down", "Left", "Right", "Front", "Back"]
Opposite = ["Up", "Down"], ["Left", "Right"], ["Front", "Back"]

cube = []
for i in range(6):
  cube.append([i,i,i,i])

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

front = cube[0]
back = cube[1]
left = cube[2]
right = cube[3]
up = cube[4]
bottom = cube[5]

frontlu = front[0]
frontru = front[1]
frontrb = front[2]
frontlb = front[3]
backlu = back[0]
backru = back[1]
backrb = back[2]
backlb = back[3]
leftlu = left[0]
leftru = left[1]
leftrb = left[2]
leftlb = left[3]
rightlu = right[0]
rightru = right[1]
rightrb = right[2]
rightlb = right[3]
uplu = up[0]
upru = up[1]
uprb = up[2]
uplb = up[3]
bottomlu = bottom[0]
bottomru = bottom[1]
bottomrb = bottom[2]
bottomlb = bottom[3]

def front: #2

  tempUlu = cube[4][0]
  tempUlbo = cube[4][3]
  cube[4][0] = cube[5][0]
  cube[4][3] = cube[5][3]
  cube[5][0] = tempUlu
  cube[5][1] = tempUlbo

  tempUlu = cube[0][0]
  tempUlbo = cube[0][3]
  cube[0][0] = cube[1][0]
  cube[0][3] = cube[1][3]
  cube[1][0] = tempUlu
  cube[1][1] = tempUlbo

  tempLlu = cube[0][0]
  tempLru = cube[0][1]
  cube[0][0] =cube[0][2]
  cube[0][1] =cube[0][2]
  cube[0][2] = tempLlu
  cube[0][3] = tempLru

def back: #2

  tempUlu = cube[4][0]
  tempUlbo = cube[4][3]
  cube[4][0] = cube[5][0]
  cube[4][3] = cube[5][3]
  cube[5][0] = tempUlu
  cube[5][1] = tempUlbo

  tempUlu = cube[0][0]
  tempUlbo = cube[0][3]
  cube[0][0] = cube[1][0]
  cube[0][3] = cube[1][3]
  cube[1][0] = tempUlu
  cube[1][1] = tempUlbo

  tempLlu = cube[2][0]
  tempLru = cube[2][1]
  cube[2][0] =cube[2][2]
  cube[2][1] =cube[2][2]
  cube[2][2] = tempLlu
  cube[2][3] = tempLru

def left: #2

  

  tempUlu = cube[4][0]
  tempUlbo = cube[4][3]
  cube[4][0] = cube[5][0]
  cube[4][3] = cube[5][3]
  cube[5][0] = tempUlu
  cube[5][1] = tempUlbo

  tempUlu = cube[0][0]
  tempUlbo = cube[0][3]
  cube[0][0] = cube[1][0]
  cube[0][3] = cube[1][3]
  cube[1][0] = tempUlu
  cube[1][1] = tempUlbo

  tempLlu = cube[2][0]
  tempLru = cube[2][1]
  cube[2][0] =cube[2][2]
  cube[2][1] =cube[2][2]
  cube[2][2] = tempLlu
  cube[2][3] = tempLru

def left: #3

  tempUlu = cube[4][0]
  tempUlbo = cube[4][3]
  cube[4][0] = cube[5][0]
  cube[4][3] = cube[5][3]
  cube[5][0] = tempUlu
  cube[5][1] = tempUlbo

  tempUlu = cube[0][0]
  tempUlbo = cube[0][3]
  cube[0][0] = cube[1][0]
  cube[0][3] = cube[1][3]
  cube[1][0] = tempUlu
  cube[1][1] = tempUlbo

  tempLlu = cube[3][0]
  tempLru = cube[3][1]
  cube[3][0] =cube[3][2]
  cube[3][1] =cube[3][2]
  cube[3][2] = tempLlu
  cube[3][3] = tempLru

def up: #5

  # 
  tempUlu = cube[4][0]
  tempUlbo = cube[4][3]
  cube[4][0] = cube[5][0]
  cube[4][3] = cube[5][3]
  cube[5][0] = tempUlu
  cube[5][1] = tempUlbo

  # up-face
  tempLlu = cube[5][0]
  tempLru = cube[5][1]
  cube[5][0] =cube[5][2]
  cube[5][1] =cube[5][3]
  cube[5][2] = tempLlu
  cube[5][3] = tempLru

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



def up(state, i = true):


def down(state, i = true):
  up(state)

def left(state, i = true):


def right(state, i = true):


def front(state, i = true):


def back(state, i = true):




#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

