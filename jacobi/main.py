# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Main code starts here:
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from steady_state_problem import define_steady_state_problem

# Number of mesh points
npoints = 64

# solve problem
define_steady_state_problem(npoints)
