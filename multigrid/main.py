# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Main code starts here:
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import switch as switch

from steady_state_problem import define_steady_state_problem
from ssp_t1 import ssp_t1
from eingenvalues import eingenvalues

# Number of mesh points
npoints = 64


test = 3
# solve problem

if test == 1:
    define_steady_state_problem(npoints)
elif test == 2:
    ssp_t1(npoints)
elif test == 3:
    eingenvalues(12)
