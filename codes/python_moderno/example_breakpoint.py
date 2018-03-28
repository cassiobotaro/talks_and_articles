# python 3.7
breakpoint()


# you change debbuger via PYTHONBREAKPOINT=pudb.set_trace
# PYTHONBREAKPOINT=0 to disable breakpoints

# pep 8 compliant
__import__('pdb').set_trace()

# old style
import pdb; pdb.set_trace()
