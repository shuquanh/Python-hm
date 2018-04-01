### START CODE HERE ### (≈ 1 line of code)
test = "Hello World"
### END CODE HERE ###

print ("test: " + test)

### -------------------------------------------------------------------------- ### 
# GRADED FUNCTION: basic_sigmoid

import math

def basic_sigmoid(x):
    """
    Compute sigmoid of x.

    Arguments:
    x -- A scalar

    Return:
    s -- sigmoid(x)
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    s = 1/(1+math.exp(-x))
    ### END CODE HERE ###
    
    return s
### -------------------------------------------------------------------------- ### 
    
basic_sigmoid(3)
 
### One reason why we use "numpy" instead of "math" in Deep Learning ###
x = [1, 2, 3]
basic_sigmoid(x) # you will see this give an error when you run it, because x is a vector.

### -------------------------------------------------------------------------- ### 

