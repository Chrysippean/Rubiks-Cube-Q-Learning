PROBLEM_DESC=\
 '''
'''
# COLORS: B: black, W: white, R: red, Y: yellow, O: orange, P: pink 
COLORS={0: 'B', 1: 'W', 2: 'R', 3: 'Y', 4: 'O', 5: 'P'}

ACTIONS = ["Up", "Down", "Left", "Right"]

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
  


# There should be 18 moves RLUDFB(6) + i(12) + 180deg(18)
# Link: https://www.rubiks.com/blog/how-to-solve-the-rubiks-cube-stage-1
#</OPERATORS>

# If i == false, then perform the inverse

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

