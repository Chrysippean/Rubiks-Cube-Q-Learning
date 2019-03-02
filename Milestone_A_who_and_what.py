#!/usr/bin/python3
'''Milestone_A_who_and_what.py
This runnable file will provide a representation of
answers to key questions about your project in CSE 415.

'''

# DO NOT EDIT THE BOILERPLATE PART OF THIS FILE HERE:

CATEGORIES=['Baroque Chess Agent','Feature-Based Reinforcement Learning for the Rubik Cube Puzzle',\
  'Hidden Markov Models: Algorithms and Applications']

class Partner():
  def __init__(self, lastname, firstname, uwnetid):
    self.uwnetid=uwnetid
    self.lastname=lastname
    self.firstname=firstname

  def __lt__(self, other):
    return (self.lastname+","+self.firstname).__lt__(other.lastname+","+other.firstname)

  def __str__(self):
    return self.lastname+", "+self.firstname+" ("+self.uwnetid+")"

class Who_and_what():
  def __init__(self, team, option, title, approach, workload_distribution, references):
    self.team=team
    self.option=option
    self.title=title
    self.approach = approach
    self.workload_distribution = workload_distribution
    self.references = references

  def report(self):
    rpt = 80*"#"+"\n"
    rpt += '''The Who and What for This Submission

Project in CSE 415, University of Washington, Winter, 2019
Milestone A

Team: 
'''
    team_sorted = sorted(self.team)
    # Note that the partner whose name comes first alphabetically
    # must do the turn-in.
    # The other partner(s) should NOT turn anything in.
    rpt += "    "+ str(team_sorted[0])+" (the partner who must turn in all files in Catalyst)\n"
    for p in team_sorted[1:]:
      rpt += "    "+str(p) + " (partner who should NOT turn anything in)\n\n"

    rpt += "Option: "+str(self.option)+"\n\n"
    rpt += "Title: "+self.title + "\n\n"
    rpt += "Approach: "+self.approach + "\n\n"
    rpt += "Workload Distribution: "+self.workload_distribution+"\n\n"
    rpt += "References: \n"
    for i in range(len(self.references)):
      rpt += "  Ref. "+str(i+1)+": "+self.references[i] + "\n"

    rpt += "\n\nThe information here indicates that the following file will need\n"+\
     "to be submitted (in addition to code and possible data files):\n"
    rpt += "    "+\
     {'1':"Baroque_Chess_Agent_Report",'2':"Rubik_Cube_Solver_Report",\
      '3':"Hidden_Markov_Models_Report"}\
        [self.option]+".pdf\n"

    rpt += "\n"+80*"#"+"\n"
    return rpt

# END OF BOILERPLATE.

# Change the following to represent your own information:

danny = Partner("Nguyen", "Daniel", "danielnn")
lillian = Partner("Lei", "Lillian", "hmlei233")
team = [lillian, danny]

OPTION = '2'
# Legal options are 1, 2, and 3.

title = "Rubik's Cube: Reinforcement Learning Approach"

approach = '''We will aim first and foremost research and understand the
fundamental methods and behaviors in Reinforcement Learning and Q-Learning,
then explore expository research sources regarding the application of these
methods to the Rubik's Cube problem. We will then investigate the various
effects of possible simplifications to the problem regarding computational
speed, and we will then implement an algorithm in Python that utilizes
these techniques to find valid solutions given any initial state.'''

workload_distribution = '''Throughout this assignment, both partners will 
work closely on all aspects of the assignment. Danny will have the main
task of researching the role of features in reinforcement learning and the
simplifications that can be made, and Lillian will mainly research the rubrics
by which the heuristics in this problem can be calculated. After research,
both partners will discuss the feasibility of each approach and choose
which methods to combine and implement in the algorithm. Both partners will
have a roughly equal role in the implementation of the code (Lillian on 
logistics, Danny on the algorithm).'''

reference1 = '''Richard Korf's paper on the Rubik's Cube;
    URL: https://courses.cs.washington.edu/courses/cse415/19wi/uwnetid/proj/korfrubik.pdf'''

reference2 = '''Poole and Mackworth's "AI" (2nd ed), Reinforcement Learning with Features,
    URL: https://artint.info/html/ArtInt_271.html'''

our_submission = Who_and_what([lillian, danny], OPTION, title, approach, workload_distribution, [reference1, reference2])

# You can run this file from the command line by typing:
# python3 who_and_what.py

# Running this file by itself should produce a report that seems correct to you.
if __name__ == '__main__':
  print(our_submission.report())
